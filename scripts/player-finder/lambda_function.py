from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime
import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient, UpdateOne

PAGES_PER_THREAD = int(os.environ["PAGES_PER_THREAD"])
MONGO_USER = os.environ["MONGO_USER"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_PORT = os.environ["MONGO_PORT"]

# We are using the playerspeed ranking as both healers and dps are in this category
wcl_web_urls = {
    3: "https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/3/10/5/Any/Any/0/0/0/0/0/?search=&page={}",  # NM Ranking
    4: "https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/4/10/5/Any/Any/0/0/0/0/0/?search=&page={}",  # HM Ranking
    5: "https://www.warcraftlogs.com/zone/rankings/table/{}/playerspeed/-1/5/20/5/Any/Any/0/0/0/0/0/?search=&page={}",  # MM Ranking
}

headers = {"Referer": "https://www.warcraftlogs.com/"}
MONGO_CLIENT = None


def connect_mongo():
    global MONGO_CLIENT

    client = MongoClient(
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@149.202.45.54:{MONGO_PORT}/?authMechanism=DEFAULT",
        serverSelectionTimeoutMS=2500,
    )
    try:
        # The ping command is cheap and does not require auth.
        client.admin.command("ping")
        MONGO_CLIENT = client.wcl
    except Exception as e:
        print(f"Unable to connect to server:\n\t{e}")


def get_players_pages(url_template, raidId, start_page, end_page, thread_id):
    print(
        f"Thread {thread_id} - Discovering players for raid {raidId} - Page {start_page} to {end_page}"
    )
    players = []

    for pageId in range(start_page, end_page):
        response = requests.get(url_template.format(raidId, pageId), headers=headers)

        if not response.ok:
            raise Exception(
                f"[WARN] Call failed ({response.status_code})\n{response.text}\n{url_template.format(raidId, pageId)}"
            )

        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.find_all("tr", {"class": ""}):

            link = row.find("a", {"target": "_blank"}, href=True)

            if link and "/character/id" in link["href"]:
                playerId = link["href"].split("/")[-2]
                players.append(int(playerId))
            else:
                continue

    print(
        f"Thread {thread_id} - Discovered {len(players)} players for raid {raidId} - Page {start_page} to {end_page}"
    )
    return players


def get_discovery_rule():
    print(f"Searching for a discovery rule outdated...")
    lte_timestamp = datetime.datetime.now() - datetime.timedelta(
        hours=int(os.environ["DELAY_DISCOVERY_IN_HOURS"])
    )
    result = MONGO_CLIENT.discovery_schedules.find_one(
        {"lastRun": {"$lte": lte_timestamp.timestamp()}}
    )
    print(f"Found a discovery rule : {result}")
    return result


def update_discovery_rule(discovery_rule):
    print(f"Updating lastRun of discovery rule...")
    MONGO_CLIENT.discovery_schedules.update_one(
        {"_id": discovery_rule["_id"]},
        {"$set": {"lastRun": datetime.datetime.now().timestamp()}},
    )


def upsert_players(players, raidId, difficulty):
    print(f"Saving players discovered infos to MongoDB...")
    requests = []
    for id in players:
        requests.append(
            UpdateOne(
                {"_id": id},
                {"$addToSet": {f"raidsToScrap.{raidId}": difficulty}},
                upsert=True,
            )
        )

    MONGO_CLIENT.discovers.bulk_write(requests, ordered=False)


def lambda_handler(event, ctx):
    all_players = []

    connect_mongo()

    discovery_rule = get_discovery_rule()

    if discovery_rule is None:
        print(
            f"No rule older than {os.environ['DELAY_DISCOVERY_IN_HOURS']} hours aborting..."
        )
        return

    nb_pages_to_discover = discovery_rule["endPage"] - discovery_rule["startPage"]
    extra_thread = int(nb_pages_to_discover % PAGES_PER_THREAD != 0)

    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = []

        for thread in range(0, nb_pages_to_discover // PAGES_PER_THREAD + extra_thread):
            thread_start_page = discovery_rule["startPage"] + thread * PAGES_PER_THREAD
            thread_end_page = (
                discovery_rule["startPage"] + (thread + 1) * PAGES_PER_THREAD
            )

            if thread_end_page > discovery_rule["endPage"]:
                thread_end_page = discovery_rule["endPage"] + 1

            tasks.append(
                executor.submit(
                    get_players_pages,
                    wcl_web_urls[discovery_rule["difficulty"]],
                    discovery_rule["raid"],
                    thread_start_page,
                    thread_end_page,
                    thread,
                )
            )
        # process completed tasks
        for future in as_completed(tasks):
            all_players.extend(future.result())

        all_players = [*set(all_players)]
        print(
            f"Total number of players discovered across all difficulties : {len(all_players)}"
        )
        upsert_players(
            all_players, discovery_rule["raid"], discovery_rule["difficulty"]
        )
        update_discovery_rule(discovery_rule)

        return {"statusCode": 200}
