import datetime
import os
import requests
import time

from pymongo import MongoClient, UpdateOne

wcl_api_url = "https://www.warcraftlogs.com/api/v2/client"
wcl_api_keys = {
    "QuantiteVerveine": {
        "key": os.environ["WCL_KEY"],
        "secret": os.environ["WCL_SECRET"],
        "token": os.environ["WCL_TOKEN"],
        "isExhausted": False,
    }
}
wcl_token_url = "https://www.warcraftlogs.com/oauth/token"
wcl_token_payload = {"grant_type": "client_credentials"}
MONGO_USER = os.environ["MONGO_USER"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_PORT = os.environ["MONGO_PORT"]

headers = {"Referer": "https://www.warcraftlogs.com/"}

MONGO_CLIENT = None

wcl_query_template = '{{"query": "query {{  \
    reportData {{ \
        {}\
    }} \
}}"}}'

wcl_api_limit_query = '{"query": "query {  \
    rateLimitData { \
        limitPerHour \
        pointsSpentThisHour \
        pointsResetIn \
    } \
}"}'


class UnknownError(Exception):
    """Unknown error, it's safer to abort run"""
    pass


class BadGateway(Exception):
    """Bad Gateway Error received from website, aborting this run"""
    pass


class ApiKeyExhausted(Exception):
    """WCL API Key return a 429 when used"""
    pass


def get_auth_token(apiKeyName, retry=False):
    global wcl_api_keys

    if wcl_api_keys[apiKeyName]["isExhausted"]:
        raise ApiKeyExhausted

    if wcl_api_keys[apiKeyName]["token"] != None:
        return wcl_api_keys[apiKeyName]["token"]

    # Token never generated on this container
    print(f"Generating auth token for {apiKeyName}...")

    response = requests.post(wcl_token_url, auth=(wcl_api_keys[apiKeyName]['key'], wcl_api_keys[apiKeyName]['secret']), data=wcl_token_payload)

    # Handling case when api point limit reach, authentication is failing too
    if response.ok:
        wcl_api_keys[apiKeyName]["token"] = response.json()["access_token"]
    elif (
        not response.ok
        and int(response.headers["x-ratelimit-remaining"]) == 0
        and int(response.headers["retry-after"]) <= 60
        and not retry
    ):
        # Hitting the API rate limit, not point limit, should sleep a bit, don't sleep to much neither cause it cost money, it's IP based and not API Key
        print(
            f"[WARN] Auth failed because rate limit reached, sleeping... ({response.status_code}) : {response.headers}"
        )
        time.sleep(int(response.headers["retry-after"]) + 1)
        return get_auth_token(apiKeyName, retry=True)
    elif not response.ok and response.status_code == 502:
        raise BadGateway
    else:
        print(
            f"[ERROR] Auth failed for unknown reason (Code : {response.status_code}, IsRetry : {retry})\n\t{response.headers}\n\t{response.text}"
        )
        raise UnknownError

    return wcl_api_keys[apiKeyName]["token"]


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


def get_reports_to_discover(lte_timestamp):
    print(
        f"Searching for a reports not actively updated since {lte_timestamp.timestamp()}..."
    )
    return MONGO_CLIENT.reports.find({"lastSeen": {"$lte": lte_timestamp.timestamp()}})


def upsert_players(players):
    print(f"Saving {len(players)} players discovered infos to MongoDB...")
    requests = []
    for id, raids in players.items():
        for raid_id, difficulties in raids.items():
            requests.append(
                UpdateOne(
                    {"_id": id},
                    {"$addToSet": {f"raidsToScrap.{raid_id}": {"$each": difficulties}}},
                    upsert=True,
                )
            )

    if len(requests) == 0:
        print("Nothing to store in mongo")
        return

    MONGO_CLIENT.discovers.bulk_write(requests, ordered=False)


def get_reports_players(reports, apiKeyName):
    headers = {
        "Authorization": f"Bearer {get_auth_token(apiKeyName)}",
        "Content-Type": "application/json",
    }
    players = {}

    query_payload = ""

    for report in reports:
        query_payload += f"Report_{report['_id']}: report(code: \\\"{report['_id']}\\\") {{ \
            rankedCharacters {{ canonicalID }}, \
            fights(killType: Kills) {{ difficulty }}, \
            zone {{id}} \
        }}"

    query = wcl_query_template.format(query_payload)
    print(wcl_api_url)
    print(query)

    response = requests.request("POST", wcl_api_url, headers=headers, data=query)

    if not response.ok:
        print(
            f"[ERROR] Unable to get reports data (Code : {response.status_code})\n\t{response.text}"
        )
        raise UnknownError
        
    for report in response.json()["data"]["reportData"].values():
        if report is None or report["rankedCharacters"] is None:
            continue
        difficulties = [*set([fight["difficulty"] for fight in report["fights"] if fight["difficulty"] is not None and fight["difficulty"] in [3, 4, 5]])]
        for player in report["rankedCharacters"]:
            if player["canonicalID"] not in players:
                players[player["canonicalID"]] = {}
            players[player["canonicalID"]][report["zone"]["id"]] = difficulties
            
    return players


def set_api_key_exhausted(apiKeyName):
    global wcl_api_keys

    wcl_api_keys[apiKeyName]["isExhausted"] = True
    wcl_api_keys[apiKeyName]["token"] = None


def get_remaining_wcl_points(apiKeyName):

    auth_token = None

    try:
        auth_token = get_auth_token(apiKeyName)
    except ApiKeyExhausted:
        return {"remaining": 0, "resetIn": 3600}

    # If API limit is reached the token will be None because auth has probably failed, so returning default data to skip this key
    result = {"remaining": 0, "resetIn": 3600}

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    response = requests.request(
        "POST", wcl_api_url, headers=headers, data=wcl_api_limit_query
    )

    if (
        not response.ok
        and response.status_code == 429
        and response.headers["retry-after"]
        and int(response.headers["retry-after"]) <= 60
    ):
        print(
            f"[WARN] Unable to get remaining budget for this key rate limit reached, sleeping...\n\t{response.headers}"
        )
        time.sleep(int(response.headers["retry-after"]) + 1)
    elif not response.ok and response.status_code == 429:
        print(
            f"[WARN] Unable to get remaining budget for this key assuming budget exhausted"
        )
        set_api_key_exhausted(apiKeyName)
        return {"remaining": 0, "resetIn": 3600}
    elif not response.ok and response.status_code == 502:
        raise BadGateway
    elif not response.ok:
        print(f"[ERROR] Unable to get remaining budget for unknown reasons")
        print(response.status_code)
        print(response.headers)
        print(response.text)
        raise UnknownError

    data = response.json()

    result["remaining"] = (
        data["data"]["rateLimitData"]["limitPerHour"]
        - data["data"]["rateLimitData"]["pointsSpentThisHour"]
    )
    result["resetIn"] = data["data"]["rateLimitData"]["pointsResetIn"]

    return result

def drop_reports(reports):
    print(f'Deleting all reports discovered in MongoDB reports collection')
    return MONGO_CLIENT.reports.delete_many({'_id':{'$in':[report['_id'] for report in reports]}})

def lambda_handler(event, ctx):
    connect_mongo()

    lte_timestamp = datetime.datetime.now() - datetime.timedelta(
        hours=int(os.environ["DELAY_REPORTS_IN_HOURS"])
    )

    reports = get_reports_to_discover(lte_timestamp)
    total_reports = len(list(reports.clone()))
    if reports is None or total_reports == 0:
        print(f"No reports older than {os.environ['DELAY_DISCOVERY_IN_HOURS']} hours aborting...")
        return

    for keyName in wcl_api_keys.keys():
        if wcl_api_keys[keyName]["isExhausted"]:
            print(f"Skipping key {keyName} marked as exhausted")
            continue

        api_budget = get_remaining_wcl_points(keyName)

        # if total_reports * 5 > api_budget["remaining"]: #Call cost 1 API point to discovery players in a report
        #     print("[WARN] Not enough budget to handle reports players discovery")
        #     continue

        reports_to_process = []
        while api_budget["remaining"] > len(reports_to_process) * 5:
            reports_to_process.append(reports.next())
            if reports_to_process[-1] is None:
                break
        
        batch_reports = []
        nb_reports_done = 0
        for report in reports_to_process:
            batch_reports.append(report)
            nb_reports_done += 1

            if len(batch_reports) % 20 == 0 or total_reports == nb_reports_done:
                players = get_reports_players(batch_reports, keyName)
                upsert_players(players)
                drop_reports(batch_reports)
                batch_reports = []

        return {"statusCode": 200}
