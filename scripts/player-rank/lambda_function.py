from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time
import boto3
import requests
import json
from datetime import datetime, timedelta
from pymongo import MongoClient, UpdateOne
import os

# The number of point used per request to WCL, approximative, this is used to stop a bit before the limit by multiplying with the number of message to process
api_call_budget = int(os.environ["WCL_CALL_BUDGET"])

wcl_token_url = "https://www.warcraftlogs.com/oauth/token"
wcl_token_payload = {"grant_type": "client_credentials"}
sqs_reports_queue = (
    "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-discovered-players"
)
sqs = boto3.client("sqs")

wcl_api_keys = {
    "marsgames": {
        "key": os.environ["WCL_KEY"],
        "token": None,
        "isExhausted": False
    }
}
wcl_api_url = "https://www.warcraftlogs.com/api/v2/client"
wcl_query_template = "{{\"query\": \"query {{  \
    characterData {{ \
        character(id: {}) {{  \
                    name, \
                    server {{ \
                    region {{ compactName }} \
                    name \
                }}, \
                {}\
        }} \
    }} \
}}\"}}"

wcl_api_limit_query = '{"query": "query {  \
    rateLimitData { \
        limitPerHour \
        pointsSpentThisHour \
        pointsResetIn \
    } \
}"}'
mongo_client = None
lambda_client = boto3.client("lambda")
lambda_function_name = os.environ["AWS_LAMBDA_FUNCTION_NAME"]
scheduler_reviver_name = os.environ["SCHEDULER_REVIVER_NAME"]
scheduler_client = boto3.client("events")


class Player:
    def __init__(self, player_data, id):
        self.load_data_from_json(player_data, id)

    def append_raids_data(self, player_data):
        player_data.pop("name", None)
        player_data.pop("server", None)

        for key, raidData in player_data.items():
            # Should not happen, but skipping data if player never kill any boss in this raid difficulty
            # Also happend when a player don't have a class defined in the app and no one hit the "update" button in the web interface
            if raidData == None or raidData["medianPerformanceAverage"] == None:
                continue

            for ranking in raidData["rankings"]:
                # Skipping undone boss in the zone
                if ranking["rankPercent"] == None:
                    continue

                self.encounters[f"{key}_{ranking['encounter']['id']}"] = {
                    "encounter": ranking["encounter"],
                    "difficulty": raidData["difficulty"],
                    "zone": raidData["zone"],
                    "metric": raidData["metric"],
                    "rankPercent": int(ranking["rankPercent"]),
                    "totalKills": ranking["totalKills"],
                    "allStars": self.get_safe_allstar_data(ranking["allStars"]),
                }

    def load_data_from_json(self, player_data, id):
        srv = player_data.pop("server")
        self.name = player_data.pop("name")
        self.id = id
        self.server = srv["name"]
        self.encounters = {}
        self.region = srv["region"]["compactName"]

        self.append_raids_data(player_data)

    def get_safe_allstar_data(self, allstar_data):
        allStarRank = 0
        allStarRegionRank = 0
        allStarServerRank = 0
        allStarRankPercent = 0

        try:
            allStarRank = int(allstar_data["rank"])
        except Exception:
            pass

        try:
            allStarRegionRank = int(allstar_data["regionRank"])
        except Exception:
            pass

        try:
            allStarServerRank = int(allstar_data["serverRank"])
        except Exception:
            pass

        try:
            allStarRankPercent = int(allstar_data["rankPercent"])
        except Exception:
            pass

        return {
            "rank": allStarRank,
            "regionRank": allStarRegionRank,
            "serverRank": allStarServerRank,
            "rankPercent": allStarRankPercent,
        }


class ApiKeyExhausted(Exception):
    """WCL API Key return a 429 when used"""

    pass


class UnknownError(Exception):
    """Unknown error, it's safer to abort run"""

    pass


class InvalidPlayerDataFormat(Exception):
    """Unknown player data format sent from the API"""

    pass

class BadGateway(Exception):
    """Bad Gateway Error received from website, aborting this run"""
    pass

def connect_mongo():
    global mongo_client
    MONGO_USER = os.environ["MONGO_USER"]
    MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
    MONGO_PORT = os.environ["MONGO_PORT"]

    client = MongoClient(
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@149.202.45.54:{MONGO_PORT}/?authMechanism=DEFAULT",
        serverSelectionTimeoutMS=2500,
    )
    try:
        # The ping command is cheap and does not require auth.
        client.admin.command("ping")
        mongo_client = client.wcl
    except Exception as e:
        print(f"Unable to connect to server:\n\t{e}")


def get_auth_token(apiKeyName, retry=False):
    global wcl_api_keys

    if wcl_api_keys[apiKeyName]["isExhausted"]:
        raise ApiKeyExhausted

    if wcl_api_keys[apiKeyName]["token"] != None:
        return wcl_api_keys[apiKeyName]["token"]

    # Token never generated on this container
    print(f"Generating auth token for {apiKeyName}...")

    headers = {"Authorization": f"Basic {wcl_api_keys[apiKeyName]['key']}"}

    response = requests.request(
        "POST", wcl_token_url, headers=headers, data=wcl_token_payload
    )

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
        abort_container_run()

    return wcl_api_keys[apiKeyName]["token"]


def set_api_key_exhausted(apiKeyName):
    global wcl_api_keys

    wcl_api_keys[apiKeyName]["isExhausted"] = True
    wcl_api_keys[apiKeyName]["token"] = None


def get_players_stats_for_player(msg, apiKeyName, players, msgId):
    playerId = msg["id"]

    headers = {
        "Authorization": f"Bearer {get_auth_token(apiKeyName)}",
        "Content-Type": "application/json",
        "Host": "www.warcraftlogs.com"
    }
    query_payload = ""
    idx = 0

    for raid in msg["raids"]:
        for difficulty in msg["raids"][raid]:
            query_payload += f"Alias_{raid}_{difficulty}: zoneRankings(byBracket: true, zoneID: {raid}, compare: Parses, difficulty: {difficulty})"
            idx += 1

    query = wcl_query_template.format(playerId, query_payload)

    response = requests.request("POST", wcl_api_url, headers=headers, data=query)

    if not response.ok:
        print(
            f"[ERROR] Unable to get player data ranks for playerId {playerId} (Code : {response.status_code})\n\t{response.text}"
        )
        return False, msgId

    try:
        player_data = response.json()["data"]["characterData"]["character"]

        if playerId in players:
            players[playerId].append_raids_data(player_data)
        else:
            players[playerId] = Player(player_data, playerId)
    except Exception as e:
        print(
            f"[WARN] Invalid player data payload (Code : {response.status_code}, Error : {e})\n\t{response.text}"
        )
        if "No class set for this character" in response.text:
            # We can't do much, player profile is not set, deleteting message to not reprocess indefinitely with an error
            return True, None
        else:
            return False, msgId

    return True, None


def upsert_players(players):
    print(f"Saving {len(players)} players to MongoDB...")

    requests = []
    for player in players.values():
        if len(player.encounters) < 1:
            continue

        set = {"name": player.name, "server": player.server, "region": player.region}

        for encounterKey, data in player.encounters.items():
            set[f"encounters.{encounterKey}"] = data
        requests.append(
            UpdateOne({"_id": int(player.id)}, {"$set": set}, upsert=True)
        )
    
    if len(requests) == 0:
        print("Nothing to add in mongo")
        return
    
    res = mongo_client.players.bulk_write(requests, ordered=False)
    print(res.bulk_api_result)


def abort_container_run():
    print("[ERROR] Unknown error, safer to abort for investigation")
    decrease_lambda_concurrency(1)
    raise UnknownError


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
        return { "remaining" : 0, "resetIn": 3600}
    elif not response.ok and response.status_code == 502:
        raise BadGateway
    elif not response.ok:
        print(f"[ERROR] Unable to get remaining budget for unknown reasons")
        print(response.status_code)
        print(response.headers)
        print(response.text)
        abort_container_run()

    data = response.json()

    result["remaining"] = (
        data["data"]["rateLimitData"]["limitPerHour"]
        - data["data"]["rateLimitData"]["pointsSpentThisHour"]
    )
    result["resetIn"] = data["data"]["rateLimitData"]["pointsResetIn"]

    return result


def can_i_run(raid_count, concurrency_count, wcl_remaining_points):
    print(
        f"Budget - Raid Count : {raid_count} - Current Concurrency : {concurrency_count} - API Call Budget : {api_call_budget} - Remaining Points : {wcl_remaining_points}"
    )

    # At any time we can assume that the function can run completely if API Limit > Lambda Instance Concurrency * api_call_budget * estimated_call_count
    # This is a greedy version as we are using this specific batch difficulties count to estimate other parallel lambda batch sizes which is potentially wrong
    # The real worst case is len(batch) * nb_raid_in_extension * nb_difficulties_in_each_raid assuming all player in a batch did all the raids in all difficulties for all the other lambdas
    # If we see too much exception from get_players_stats_for_player we should move to this worst case instead
    if wcl_remaining_points > concurrency_count * api_call_budget * raid_count:
        return True
    else:
        return False


def scheduler_reviver_run(resetIn):
    invokeDate = datetime.now() + timedelta(seconds=resetIn + 30)
    print(f"It is now @ {datetime.now()}")
    print(f"Scheduling reviver @ {invokeDate.isoformat()}")

    scheduler_client.put_rule(
        Name=scheduler_reviver_name,
        ScheduleExpression=f"cron({invokeDate.minute} {invokeDate.hour} {invokeDate.day} {invokeDate.month} ? {invokeDate.year})",
        State="ENABLED",
    )


def decrease_lambda_concurrency(concurrency_count):
    lambda_client.put_function_concurrency(
        FunctionName=lambda_function_name,
        ReservedConcurrentExecutions=concurrency_count - 1,
    )


def get_raid_count_from_batch(batch):
    count = 0

    for msg in batch:
        for raid_difficulties in msg["raids"]:
            count += len(raid_difficulties)

    return count


def lambda_handler(event, ctx):
    concurrency_count = lambda_client.get_function_concurrency(
        FunctionName=lambda_function_name
    )["ReservedConcurrentExecutions"]

    minResetIn = 3600
    json_messages = [json.loads(record["body"]) for record in event["Records"]]
    print(f"Starting lambda with {len(json_messages)} new SQS messages")

    for keyName in wcl_api_keys.keys():
        if wcl_api_keys[keyName]["isExhausted"]:
            print(f"Skipping key {keyName} marked as exhausted")
            continue

        api_budget = get_remaining_wcl_points(keyName)
        call_count = get_raid_count_from_batch(json_messages)

        if can_i_run(call_count, concurrency_count, api_budget["remaining"]):
            print("Enough budget to handle all the calls, proceeding with players...")
            if mongo_client == None:
                connect_mongo()

            players = {}

            # Multithread is more a headache than a solution here, better go with simple for loop
            # Nightmare to manage multithread + lambda concurrency and handle all the rate limit errors
            with ThreadPoolExecutor(max_workers=1) as executor:
                tasks = []
                msgIdx = 0
                for msg in json_messages:
                    tasks.append(
                        executor.submit(
                            get_players_stats_for_player,
                            msg,
                            keyName,
                            players,
                            event["Records"][msgIdx]["messageId"],
                        )
                    )
                    msgIdx += 1

                failed_messages = []

                for future in as_completed(tasks):
                    if future.result()[0] == False:
                        failed_messages.append(future.result()[1])

                upsert_players(players)

                if len(failed_messages) > 0:
                    return {
                        "batchItemFailures": [
                            {
                                "itemIdentifier": messageId
                                for messageId in failed_messages
                            }
                        ]
                    }
                else:
                    return {"statusCode": 200}
        else:
            print(f"Not enough budget for key {keyName} to run all messages...")

            if api_budget["resetIn"] < minResetIn:
                minResetIn = api_budget["resetIn"]

    print(
        "No API Key found with enough budget to handle all the calls decreasing concurrency..."
    )
    decrease_lambda_concurrency(concurrency_count)

    if concurrency_count == 1:
        print(
            f"Lambda has been disabled, scheduling the reviver func to run in at least {minResetIn} seconds"
        )
        scheduler_reviver_run(minResetIn)

    # Safeguard to not delete SQS message which is the default behavior when lambda exit with success
    return {
        "batchItemFailures": [
            {"itemIdentifier": msg["messageId"] for msg in event["Records"]}
        ]
    }
