from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient, UpdateOne


#We are using the playerspeed ranking as both healers and dps are in this category
wcl_web_urls = {
    3:"https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/3/10/5/Any/Any/0/0/0/0/0/?search=&page={}", #NM Ranking
    4:"https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/4/10/5/Any/Any/0/0/0/0/0/?search=&page={}", #HM Ranking
    5:"https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/5/20/5/Any/Any/0/0/0/0/0/?search=&page={}" #MM Ranking
}

headers = {
    "Referer" :  "https://www.warcraftlogs.com/"
}
mongo_client = None

def connect_mongo():
    global mongo_client
    MONGO_USER = os.environ['MONGO_USER']
    MONGO_PASSWORD = os.environ['MONGO_PASSWORD']
    MONGO_PORT = os.environ['MONGO_PORT']

    client = MongoClient(
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@149.202.45.54:{MONGO_PORT}/?authMechanism=DEFAULT",
        serverSelectionTimeoutMS=2500
    )
    try:
        # The ping command is cheap and does not require auth.
        client.admin.command("ping")
        mongo_client = client.wcl
    except Exception as e:
        print(f"Unable to connect to server:\n\t{e}")

def get_players_pages(url_template, raidId, pageLimit):
    print(f"Discovering players for raid {raidId} @ {url_template}")
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

def upsert_players(players, raidId, difficulty):
    print(f"Saving {len(players)} players to MongoDB")
    requests = []
    for id in players:
        requests.append(
            UpdateOne({"_id": id}, { "$push": { f"raidsToScrap.{raidId}": difficulty } }, upsert=True)
        )
    
    mongo_client.discovers.bulk_write(requests, ordered=False)

def lambda_handler(event, ctx):
    raid = event["raid"]
    difficulty = event["difficulty"]
    pageLimit = event["pageLimit"]
    all_players = []
    
    connect_mongo()
    all_players = get_players_pages(wcl_web_urls[raid], raid, pageLimit)
    print(f"Total number of players discovered for raid {raid} and difficulty {difficulty}: {len(all_players)}")
    upsert_players(all_players, raid, difficulty)
    #with ThreadPoolExecutor(max_workers=len(wcl_web_urls)) as executor:
        #tasks = [executor.submit(get_players_pages, url, raid, pageLimitFrom, pageLimitTo) for url in wcl_web_urls]
        
        # process completed tasks
        #for future in as_completed(tasks):
        #    all_players.extend(future.result())

        #all_players = [*set(all_players)]
        #print(f"Total number of players discovered across all difficulties from page {pageLimitFrom} to page {pageLimitTo} : {len(all_players)}")
        #upsert_players(all_players, raid)

        #return {
        #    'statusCode': 200
        #}