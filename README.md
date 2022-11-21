1. pip install pipenv
2. cd report-id
3. pipenv install
4. Take env path and put it in create_lambda_archive.sh & replace path to repo root

############## Amazon Stuff ###############
1. WCLPlayerDiscover (player-finder in git) lambda is triggered every 36 hours through EventBirdge events
It scraps all pages of player on WCL raid by raid, so there is 3 event (3 raids for current extension) calling the lambda with a payload like
{
  "raids": [
    26
  ]
}
It uses env var WCL_PAGE_LIMIT to get the max amount of page to scrap (250 now around 10 min to scrap for 1 raid)
1 raid & 250 page = around 30k messages

Then it push messages in wcl-discovered-players SQS queue formatted like : 

{"id": 58553935, "raidsRank": {"26": 174}}

2. WCLGetPlayerRanks Lambda (player-rank in git) is triggered with any new message in wcl-discovered-players SQS queue
It run with 10 messages batch & 1 concurrent lamdba max to cstay under the 72k WCL API limit
It get players data for all boss of the raid specified in the message, format this and insert into the MongoDB

3. Every 2 day WCLGenerateDB (db-generator in git) Lambda run to read the whole MongoDB, generate the lua formatted db and git commit automatically