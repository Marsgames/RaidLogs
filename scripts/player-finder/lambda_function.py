import boto3
import requests
import json
from bs4 import BeautifulSoup
import os

sqs = boto3.client('sqs')

wcl_web_url = "https://www.warcraftlogs.com/zone/rankings/table/{0}/playerspeed/-1/5/20/5/Any/Any/0/0/0/0/0/?search=&page={1}"
headers = {
    "Referer" :  "https://www.warcraftlogs.com/"
}

renamedPlayerCount = 0
gqlCallCount = 0
sqs_max_batch_size = 10
sqs_player_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-discovered-players"

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def send_discovered_players_in_queue(players):
    
    print(f'Sending playerId\'s in queue...')
    #Ids should be unique in the batch
    formatted_messages = [{"Id": str(id), "MessageBody":json.dumps(player)} for id, player in players.items()]
    for batch in list(split(formatted_messages, sqs_max_batch_size)):
        sqs.send_message_batch(QueueUrl=sqs_player_queue, Entries=batch)

def get_players_page(raidId, pageId, players):
    global renamedPlayerCount
    global gqlCallCount
    
    response = requests.get(wcl_web_url.format(raidId, pageId), headers=headers)

    if not response.ok:
        print(f"[WARN] Call failed ({response.status_code})\n{response.text}")
    
    soup = BeautifulSoup(response.text, "html.parser")

    for row in soup.find_all("tr", { "class" : ""}):

        link = row.find("a", { "target" : "_blank"}, href=True)

        if link and "/character/id" in link["href"]:
            playerId = link["href"].split('/')[-2]
            rank = row["id"].split('-')[-1]
            player = {"id": int(playerId), "rank": int(rank), "raidId": int(raidId)}

            #New player not in list yest
            if player["id"] not in players:
                players[player["id"]] = {"id" : player["id"], "raidsRank": {}}
            #Player with same id but different name, that's a rename
            else:
                if player["raidId"] in players[player["id"]]["raidsRank"]:
                    renamedPlayerCount += 1
            
            gqlCallCount += 1
            players[player["id"]]["raidsRank"][player["raidId"]] = player["rank"]
        else:
            continue
    
    return players

def lambda_handler(event, ctx):
    global renamedPlayerCount
    global gqlCallCount

    renamedPlayerCount = 0
    gqlCallCount = 0

    raids = event["raids"]
    pageLimit = int(os.environ['WCL_PAGE_LIMIT'])
    players = {}

    for raidId in raids:
        for pageId in range(1, pageLimit):
            print(f"Scrapping page {pageId} for raid {raidId}")
            players = get_players_page(raidId, pageId, players)

    print(f"Number of players discovered : {len(players)}")
    print(f"Number of API call to get all player raid stats : {gqlCallCount}")
    print(f"Potential duplicates for renaming : {renamedPlayerCount}")

    send_discovered_players_in_queue(players)

    return {
        'statusCode': 200
    }