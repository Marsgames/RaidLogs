############## Package Lambda Func #############
1. pip install pipenv
2. cd /path/to/lambda/folder && pipenv install #This will create a pipenv with dependencies for this lambda using the Pipfile
3. In each lambda folder, there is a `create_lambda_archive.sh` file, replace `VENV_PATH` with path printed at step 3 and GIT_SCRAPPER_PATH with the path to the lambda folder

############## AWS Budget #################

1. WCLPlayerDiscover
600 pages to scrap = 550 seconds
Running with 256 Mb

Approx 5600 pages to scrap every 24h
5600 pages = 5140 seconds
5140 seconds * 30 days * 0.256 = 40k GB Seconds

2. WCLPlayerDiscoverAggregator
3. WCLGetPlayerRanks
4. WCLGenerateDB

5. SQS Queue

############## Amazon Stuff ###############

WCLPlayerDiscover (player-finder in git) 
1. The lambda is triggered every 30 minutes through EventBridge scheduler <br>
2. It looks for a discovery rule in the `discovery_schedules` collection of Mongo that hasn't been run since at least DELAY_DISCOVERY_IN_HOURS (24) hours
```
{
  "_id": {
    "$oid": "638190fc00bc58421e002c83"
  },
  "raid": 26,
  "difficulty": 3,
  "startPage": 1,
  "endPage": 600,
  "lastRun": {
    "$date": {
      "$numberLong": "1669438300480"
    }
  }
}
```
3. If a rule is found, it breaks down the total number of pages to scrap in chunks of PAGES_PER_THREAD (200) and process the chunks using multiple threads in parallel (5 max currently hardcoded)
4. All the discovered players are then saved in the `discovers` collection in Mongo
```
{
  "_id": 57147396,
  "raidsToScrap": {
    "26": [
      3,
      5
    ],
    "28": [
      3,
      4,
      5
    ]
  }
}
```
5. The `lastRun` field of the discovery rule used is then updated with the current timestamp

Note : 
- We can't run "unlimited" parallel thread with a massive amount of pages because the website then blacklist temporarily the Lambda IP address
- Currently 3 to 5 thread with 200 pages each and 256 MB (more RAM means more powerfull thread in Lambda, so few RAM mean slower thread and helps staying under the radar) works
- More than 800 pages in one thread or even 1000 pages on 7 thread and 512 MB RAM and the Lambda reach the max timeout

WCLPlayerDiscoverAggregator (player-finder-aggregator in git) 
1. The lambda is triggered every few hours through EventBridge scheduler
2. If all discovery rule in the `discovery_schedules` collection are less than 24 hours (means we have scrapped all the players for the day) then it continue
3. It loads data from the `discovers` mongo collection
4. Push all the data loaded into the `wcl-discovered-players` SQS queue (same format than in mongo)
5. It empty the `discovers` mongo collection

Note : 
- It is important to run after all the scrapping jobs for the day made by WCLPlayerDiscover are done because we then know exactly which raids and difficulty a player have participated in.
- With exact participation of a player we can query only for the specific raid/difficulty boss data from WCL API
- We create only 1 SQS message per player aggregated from the different asynchronous scrapping job which are focused only on a specific raid & difficulty pair (1 message per player vs 1 message per player per raid per difficulty)

WCLGetPlayerRanks (player-rank in git)
1. The lambda is triggered as soon as there are messages in the `wcl-discovered-players` SQS queue
2. Each lambda receive a batch of messages from the SQS queue (5 currently, configurable in the trigger)
3. First the lambda get remaining points for each of the API key in the pool
4. The lambda evaluates if in the WCL API key pool there is a key with enough remaining points to process all it's messages using the following strategy :
  a. For each messages (1 per player), it looks at all the difficulties the player have participated and do a global sum, for example with five messages like this one : 
```
{
  "id": 57147396,
  "raidsToScrap": {
    "26": [
      3,
      5
    ],
    "28": [
      3,
      4,
      5
    ]
  }
}
```
  5 messages * 5 Difficulties (2 in 26 and 3 in 28) = 25
  b. As the WCLGetPlayerRanks is runned in parallel, it query the AWS API for the current concurrency limit for this lambda (at any moment in time there might be X concurrent lambda doing the same work so we estimate the worst case)
  c. It use the WCL_CALL_BUDGET env var, which is roughly the cost of querying all boss data for 1 player in 1 raid in 1 difficulty
  d. It multiplies then the WCL_CALL_BUDGET * current concurrency limit * total difficulties in the message batch (25 in example) = Total requires number of API point to process the batch of messages
4. If an API have enough remaining points, then the lambda process the messages
  a. For each message, build the query based on the difficulties the player participated in
  b. Run the query
  c. Format data
  d. Save them in the `players` mongo collection
5. If no API key have enough points remaining, the lambda reduce the current concurrency limit by 1 and throw an exception
6. If the concurrency limit reach 0, it schedule the WCLReviver lambda to be called as soon as an API key points limit reset

Note : 
- The WCLReviver function is critical because once the concurrency limit has been set to 0 on a lambda it can't be run, even if there are still messages in the queue
- On the other hand there is no need to execute the lambda (eating lambda execution time budget) if no API keys have points remaining
- SQS messages received by the lambda are automatically deleted if the lambda execute successfully, that's why we throw an exception when we don't have enough theorical API budget so there sent back to the queue to be reprocessed after

WCLReviver (reviver in git)
1. This lambda is executed at some point in time using an Eventbridge scheduler
2. The only action of this lambda is to set the concurrency limit of LAMBDA_TO_REVIVE env var (WCLGetPlayerRanks) to CONCURRENCY_LIMIT (50)

Note : 
- The scheduler which trigger the execution of this lambda is updated by WCLGetPlayerRanks to run few seconds after the first api key budget resets

WCLGenerateDB (db-generator in git)
1. Triggered every 24 hours using Eventbridge scheduler
2. Clone the project git repository 
3. Get all the player data by region and server from the `players` mongo collection
4. Uglify them (generate reverse mapping etc...) and create the LUA table string
5. Save each regional database in it's own file
6. Save tooling for reverse mapping of uglified data
7. Commit and push the new databases in the repository

Note :
- The lambda is running with more RAM than any other to allow all the Mongo data to fit in memory, reducing call between lambda and mongo and speeding the whole process
- Building the lua strings requires a bunch of memory too
