from concurrent.futures import ThreadPoolExecutor, as_completed
import boto3
import requests
import json
from bs4 import BeautifulSoup
import os

sqs = boto3.client('sqs')

#We are using the playerspeed ranking as both healers and dps are in this category
wcl_web_urls = [
    "https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/4/10/5/Any/Any/0/0/0/0/0/?search=&page={}", #HM Ranking
    "https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/3/10/5/Any/Any/0/0/0/0/0/?search=&page={}", #NM Ranking
    "https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/5/20/5/Any/Any/0/0/0/0/0/?search=&page={}" #MM Ranking
]

headers = {
    "Referer" :  "https://www.warcraftlogs.com/"
}

sqs_max_batch_size = 10
sqs_player_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-discovered-players"

def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def send_discovered_players_in_queue(players, raid):
    print(f'Sending playerId\'s in queue...')
    #Ids should be unique in the batch
    formatted_messages = [{"Id": str(id), "MessageBody":json.dumps({id:raid})} for id in players]
    for batch in list(split(formatted_messages, sqs_max_batch_size)):
        sqs.send_message_batch(QueueUrl=sqs_player_queue, Entries=batch)
    print(f'Players saved in queue')

def get_players_pages(url_template, raidId):
    print(f"Discovering players for raid {raidId} @ {url_template}")
    pageLimit = int(os.environ['WCL_PAGE_LIMIT'])
    players = []

    for pageId in range(1, pageLimit):
        response = requests.get(url_template.format(raidId, pageId), headers=headers)

        if not response.ok:
            print(f"[WARN] Call failed ({response.status_code})\n{response.text}\n{url_template.format(raidId, pageId)}")
        
        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.find_all("tr", { "class" : ""}):

            link = row.find("a", { "target" : "_blank"}, href=True)

            if link and "/character/id" in link["href"]:
                playerId = link["href"].split('/')[-2]
                players.append(int(playerId))
            else:
                continue
    
    print(f"Discovered {len(players)} players for raid {raidId} @ {url_template}")
    return players

def lambda_handler(event, ctx):
    raid = event["raid"]
    all_players = []

    with ThreadPoolExecutor(max_workers=len(wcl_web_urls)) as executor:
        tasks = [executor.submit(get_players_pages, url, raid) for url in wcl_web_urls]
        
        # process completed tasks
        for future in as_completed(tasks):
            all_players.extend(future.result())

        all_players = [*set(all_players)]
        print(f"Total number of players discovered across all difficulties : {len(all_players)}")

        send_discovered_players_in_queue(all_players, raid)

        return {
            'statusCode': 200
        }