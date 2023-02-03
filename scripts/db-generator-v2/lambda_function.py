import boto3
import os
import decimal
import json

from pymongo import MongoClient

# Generate DB for EU
# Create a sqs message for next region
# Send message to sqs
# If region is EU, generate git tag and push

sqs_db_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl_db_generator"
lambda_client = boto3.client("lambda")

git_repo_url = "https://Marsgames:{0}@github.com/Marsgames/WarLogs.git"
git_repo_path = "/tmp/WarLogs"
wow_regions = ["TW", "KR", "CN", "US", "EU"]
nbPlayers = 0
mapping = []

########## Mongo DB ##########
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
########## Mongo DB ##########

########## Generate DB ##########
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

def dump_lua(data):
    if type(data) is str:
        return f'"{data}"'
    if type(data) in (int, float) or isinstance(data, decimal.Decimal):
        return f"{data}"
    if type(data) is bool:
        return data and "true" or "false"
    if type(data) is list:
        l = "{"
        l += ", ".join([dump_lua(item) for item in data])
        l += "}"
        return l
    if type(data) is dict:
        t = "{"
        t += ", ".join(
            [
                f'["{k}"]={dump_lua(v)}' if type(k) is str else f"[{k}]={dump_lua(v)}"
                for k, v in data.items()
            ]
        )
        t += "}"
        return t

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
########## Generate DB ##########

########## Mapping ##########
def generate_reverse_mapping():
    global mapping

    with open(f"{git_repo_path}/db/WL_DB_Tools.lua", "w") as db_file:
        gnippam = {}
        for k, v in enumerate(mapping):
            gnippam[k] = {
                "difficulty": int(v.split(":")[1]),
                "encounter": int(v.split(":")[0]),
                "metric": v.split(":")[2],
            }

        print(f"Saving reverse mapping...")
        print(gnippam)
        db_file.write(
            f"local _, ns = ...\nlocal gnippam = {dump_lua(gnippam)}\nns.gnippam = gnippam"
        )
########## Mapping ##########

########## Tools ##########
def update_toc():
    # Open WarLogs.toc to update a line
    major, minor, patch = "X", "X", "X"
    with open(f"{git_repo_path}/WarLogs.toc", "r") as toc_file:
        lines = toc_file.readlines()
        for i, line in enumerate(lines):
            if line.startswith("## Version"):
                actual_version = line.split(" ")[2]
                major, minor, patch = actual_version.split(".")
                patch = int(patch) + 1
                lines[i] = f"## Version: {major}.{minor}.{patch}\n"
    with open(f"{git_repo_path}/WarLogs.toc", "w") as toc_file:
        toc_file.writelines(lines)
    return f"{major}.{minor}.{patch}"

def get_next_region(current_region):
    return wow_regions[(wow_regions.index(current_region) + 1) % len(wow_regions)]

def send_sqs_message(message):
    sqs = boto3.client("sqs")
    sqs.send_message(QueueUrl=sqs_db_queue, MessageBody=message)
########## Tools ##########

########## Git ##########
def clone_git_repo():
    if os.path.exists(git_repo_path):
        print(f"Git repo already cloned, pulling...")
        os.system(f"cd {git_repo_path} && git pull")
    else:
        print(f"Cloning git repo...")
        os.system(
            f"git clone {git_repo_url.format(os.environ['GIT_TOKEN'])} {git_repo_path}"
        )

def commit(region):
    global nbPlayers

    print(f"Commiting new db...")
    os.system(
        f"cd {git_repo_path} && git config user.email 'aws@aws.com' && git config user.name 'AWS Lambda' && git add * && git commit -m 'Auto Generated DB' -m 'DB for region {region} generated' && git push"
    )

def generate_tag():
    version = update_toc()
    os.system(f"cd {git_repo_path} && git tag {version} && git push --tags")
    # Creating a release on github requires "gh" cli, but I'm not sure it's installed on lambda so flemme
    # os.system(f'cd {git_repo_path} && git release create {version} -F <(echo "WarLogs {version}")')
########## Git ##########

def lambda_handler(event, context):
    global mapping
    global nbPlayers
    mapping = []
    region = "TW"
    nbPlayers = 0

    # Connect to mongoDB
    db = get_mongo_db()

    # Try get current region
    if "region" in event:
        region = event["region"]
    if "nbPlayers" in event:
        nbPlayers = event["nbPlayers"]

    # Generate DB for region
    generate_db(db, region)

    # Generate mapping for region
    generate_reverse_mapping()

    # Clone git repo
    clone_git_repo()

    # if region is not eu, create a sqs message for next region and send it to sqs
    if region != "EU":
        # Create a sqs message for next region
        next_region = get_next_region(region)
        message = {
            "region": next_region,
            "nbPlayers": nbPlayers,
        }
        # Send message to sqs
        send_sqs_message(message)
    else:
        # Generate git tag
        generate_tag()

    # push modifications to git
    commit(region)