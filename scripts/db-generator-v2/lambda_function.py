import boto3
import decimal
import os

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
    cursor = inDB.players.find(
        {"region": forRegion, "server": forServer}, batch_size=1000
    )
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
        print(f"There is {len(region_servers)} servers in {forRegion}")
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
        lines.append(f'\n_G["WL_DB_{forRegion}"] = provider')
        # lines.append("\nWarLogsAddCharsToDB(provider)")
        db_file.writelines(lines)

    return forRegion


########## Generate DB ##########

########## Mapping ##########
def generate_reverse_mapping(region):
    global mapping

    with open(f"{git_repo_path}/db/WL_DB_Tools_{region}.lua", "w") as db_file:
        gnippam = {}
        for k, v in enumerate(mapping):
            gnippam[k] = {
                "difficulty": int(v.split(":")[1]),
                "encounter": int(v.split(":")[0]),
                "metric": v.split(":")[2],
            }

        print(f"Saving reverse mapping...")
        # print(gnippam)
        db_file.write(
            f'local _, ns = ...\nlocal gnippam = {dump_lua(gnippam)}\n_G["{region}_gnippam"] = gnippam'
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


def send_sqs_message(attributes):
    sqs = boto3.client("sqs")
    message = "Updating DB"
    sqs.send_message(
        QueueUrl=sqs_db_queue,
        MessageBody=message,
        MessageAttributes=attributes,
    )


def remove_tmp_folder():
    if os.path.exists(git_repo_path):
        os.system(f"rm -rf {git_repo_path}")


########## Tools ##########

########## Git ##########
def clone_git_repo():
    if not os.path.exists(git_repo_path):
        print(f"Cloning new git repo...")
        # os.system(f"mkdir -p {git_repo_path}/db")
        os.system(
            f"git clone {git_repo_url.format(os.environ['GIT_TOKEN'])} {git_repo_path}"
        )
        print(f"Git repo cloned")

    print("Updating git repo...")
    os.system(f"cd {git_repo_path} && git pull")

    if not os.path.exists(f"{git_repo_path}/db"):
        os.system(f"cd {git_repo_path} && mkdir db")
        print(
            "We'll have an issue, beacause the db folder is missing, so what else is missing ?"
        )


def commit(region):
    global nbPlayers

    os.system(
        f"cd {git_repo_path} && git config user.email 'aws@aws.com' && git config user.name 'AWS Lambda' && git add * && git commit -m 'Auto Generated {region} DB' -m 'DB for region {region} generated\n{nbPlayers} players processed' && git push"
    )


def generate_tag():
    version = update_toc()
    os.system(
        f"cd {git_repo_path} && git config user.email 'aws@aws.com' && git config user.name 'AWS Lambda' && git add * && git commit -m 'Auto Generated {version} tag' && git push"
    )
    os.system(f"cd {git_repo_path} && git tag {version} && git push --tags")

    # Creating a release on github requires "gh" cli, but I'm not sure it's installed on lambda so flemme
    # os.system(f'cd {git_repo_path} && git release create {version} -F <(echo "WarLogs {version}")')


########## Git ##########


def lambda_handler(event, context):
    global mapping
    global nbPlayers
    mapping = []
    wowRegion = "TW"
    nbPlayers = 0

    # Connect to mongoDB
    print("Connecting to MongoDB...")
    db = get_mongo_db()

    # Try get current wowRegion
    print("Getting current wowRegion and nbPlayers...")
    # if there is records
    if "Records" in event:
        for record in event["Records"]:
            attributes = record["messageAttributes"]
            if "wowRegion" in attributes:
                wowRegion = attributes["wowRegion"]["stringValue"]
            if "nbPlayers" in attributes:
                nbPlayers = int(attributes["nbPlayers"]["stringValue"])

            # Clone git repo
            print("Cloning git repo...")
            clone_git_repo()

            # Generate DB for wowRegion
            print(f"Generating DB for {wowRegion}...")
            generate_db(db, wowRegion)

            # Generate mapping for wowRegion
            print(f"Generating mapping for {wowRegion}...")
            generate_reverse_mapping(wowRegion)

            # push modifications to git
            print("Committing to git...")
            commit(wowRegion)

            # if wowRegion is not eu, create a sqs message for next wowRegion and send it to sqs
            if wowRegion != "EU":
                # Create a sqs message for next wowRegion
                next_region = get_next_region(wowRegion)
                attributes = {"wowRegion": {}, "nbPlayers": {}}
                attributes["wowRegion"]["StringValue"] = next_region
                attributes["nbPlayers"]["StringValue"] = str(nbPlayers)
                # Send message to sqs
                print(
                    f"Sending message to SQS for wowRegion {next_region}, with {nbPlayers} players..."
                )
                send_sqs_message(attributes)
            else:
                # Generate git tag
                print("Generating git tag...")
                generate_tag()

            remove_tmp_folder()

    else:
        # Clone git repo
        print("Cloning git repo...")
        clone_git_repo()

        # Generate DB for wowRegion
        print(f"Generating DB for {wowRegion}...")
        generate_db(db, wowRegion)

        # Generate mapping for wowRegion
        print(f"Generating mapping for {wowRegion}...")
        generate_reverse_mapping(wowRegion)

        # push modifications to git
        print("Committing to git...")
        commit(wowRegion)

        # if wowRegion is not eu, create a sqs message for next wowRegion and send it to sqs
        if wowRegion != "EU":
            # Create a sqs message for next wowRegion
            next_region = get_next_region(wowRegion)
            attributes = {"wowRegion": {}, "nbPlayers": {}}
            attributes["wowRegion"]["StringValue"] = next_region
            attributes["nbPlayers"]["StringValue"] = str(nbPlayers)
            # Send message to sqs
            print(
                f"Sending message to SQS for wowRegion {next_region}, with {nbPlayers} players..."
            )
            send_sqs_message(attributes)
        else:
            # Generate git tag
            print("Generating git tag...")
            generate_tag()

        remove_tmp_folder()
