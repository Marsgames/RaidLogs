import boto3
import os

from pymongo import MongoClient

# Generate DB for EU
# Create a sqs message for next region
# Send message to sqs
# If region is EU, generate git tag and push

sqs_db_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl_db_generator"
sqs = boto3.client("sqs")
lambda_client = boto3.client("lambda")

git_repo_url = "https://Marsgames:{0}@github.com/Marsgames/WarLogs.git"
git_repo_path = "/tmp/WarLogs"
wow_regions = ["EU", "CN", "KR", "TW", "US"]
nbPlayers = 0

mapping = []

def get_mongo_db():
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
        return client.wcl
    except Exception as e:
        print(f"Unable to connect to server:\n\t{e}")

def get_players(inDB, forRegion, forServer):
    cursor = inDB.players.find({"region": forRegion, "server": forServer}, batch_size=1000)
    return cursor

# Get a "hash" kind of value for a specific difficulty/encounter/metric combination
def get_hash(d, e, m):
    global mapping
    val = f"{e}:{d}:{m}"
    if val not in mapping:
        mapping.append(val)

    return mapping.index(val)

def transform_player_data_ugly(player):
    tmp_player_data = []
    for encounter in player["encounters"].values():
        # Temp fix waiting for all db to be updated, should be removed in 1 or 2 day
        encounterId = 0
        if type(encounter["encounter"]) == int:
            encounterId = encounter["encounter"]
        else:
            encounterId = encounter["encounter"]["id"]
        tmp_player_data.append(
            f"{get_hash(encounter['difficulty'], encounterId, encounter['metric'])}:{encounter['rankPercent']}:{encounter['totalKills']}"
        )

    return "/".join(tmp_player_data)

def generate_db(withDB, forRegion):
    global nbPlayers
    with open(f"{git_repo_path}/db/WL_DB_{forRegion}.lua", "w") as db_file:
        region_servers = withDB.players.distinct("server", {"region": forRegion})
        lines = []
        # Add header
        lines.append("local provider = {}\n")
        lines.append("local F\n\n")
        # Add database
        for server in region_servers:
            tmp_db = {server: {}}
            players = get_players(withDB, forRegion, server)
            for player in players:
                tmp_db[server][player["name"]] = transform_player_data_ugly(player)
            nbPlayers += len(tmp_db[server])
            print(f"Found {len(tmp_db[server])} players on {forRegion}-{server}")
            lua_dump = dump_lua(tmp_db)
            lua_dump = lua_dump[1:-1]
            line = f"F = function() provider{lua_dump} end F()\n"
            lines.append(line)
        # Add footer
        lines.append("\nWarLogsAddCharsToDB(provider)")
        db_file.writelines(lines)

    return forRegion


def lambda_handler(event, context):
    global mapping
    global nbPlayers
    mapping = []
    nbPlayers = 0

    # Connect to mongoDB
    db = get_mongo_db()

    # Get current region
    region = event["region"]

    # Generate DB for region
    generate_db(db, region)

    # Generate mapping for region

    # Clone git repo

    # if region is not eu, create a sqs message for next region and send it to sqs

    # if region is eu, generate git tag and push
    # if regionn is eu, update toc file

    # push modifications to git



    print(event)
    if event["region"] == "EU":
        print("Generating git tag")
        # Generate git tag
        # Push git tag
    else:
        # Create a sqs message for next region
        # Send message to sqs
        pass