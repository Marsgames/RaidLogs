from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import decimal
from pymongo import MongoClient

git_repo_url = "https://{0}@github.com/Marsgames/WarLogs.git"
git_repo_path = "/tmp/WarLogs"
wow_regions = ["EU", "CN", "KR", "TW", "US"]

mapping = []

def get_mongo_db():
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
        return client.wcl
    except Exception as e:
        print(f"Unable to connect to server:\n\t{e}")

def get_players(db, region, server):
    cursor = db.players.find({"region": region, "server": server}, batch_size=1000)
    return cursor

def clone_git_repo():
    if os.path.exists(git_repo_path):
        print(f"Git repo already cloned, pulling...")
        os.system(f"cd {git_repo_path} && git pull")
    else:
        print(f"Cloning git repo...")
        os.system(f"git clone {git_repo_url.format(os.environ['GIT_TOKEN'])} {git_repo_path}")

def dump_lua(data):
    if type(data) is str:
        return f'"{data}"'
    if type(data) in (int, float) or isinstance(data, decimal.Decimal):
        return f'{data}'
    if type(data) is bool:
        return data and "true" or "false"
    if type(data) is list:
        l = "{"
        l += ", ".join([dump_lua(item) for item in data])
        l += "}"
        return l
    if type(data) is dict:
        t = "{"
        t += ", ".join([f'[\"{k}\"]={dump_lua(v)}' if type(k) is str else f'[{k}]={dump_lua(v)}' for k,v in data.items()])
        t += "}"
        return t

#Get a "hash" kind of value for a specific difficulty/encounter/metric combination
def get_hash(d, e, m):
    global mapping
    val = f"{e}:{d}:{m}"
    if val not in mapping:
        mapping.append(val)

    return mapping.index(val)

def transform_player_data_ugly(player):
    tmp_player_data = []
    for raid in player["raids"].values():
        tmp_player_data.append(f"{get_hash(raid['difficulty'], raid['encounter'], raid['metric'])}:{raid['bestPerformance']}:{raid['averagePerformance']}:{raid['totalKills']}")
    
    return '/'.join(tmp_player_data)

def generate_db(db, region):
    with open(f"{git_repo_path}/db/WL_DB_{region}.lua", "w") as db_file:
        region_servers = db.players.distinct("server", {"region" : region})
        lines = []
        for server in region_servers:
            tmp_db = {server: {}}
            players = get_players(db, region, server)
            for player in players: 
                tmp_db[server][player["name"]] = transform_player_data_ugly(player)
            print(f"Found {len(tmp_db[server])} players on {region}-{server}")
            lines.append(f"WarLogsAddCharsToDB({dump_lua(tmp_db)})\n")
        db_file.writelines(lines)
    
    return region

def generate_reverse_mapping():
    global mapping

    with open(f"{git_repo_path}/db/WL_DB_Tools.lua", "w") as db_file:
        gnippam = {}
        for k, v in enumerate(mapping):
            gnippam[k] = { "difficulty": int(v.split(':')[1]), "encounter": int(v.split(':')[0]), "metric" : v.split(':')[2] }
        
        print(f"Saving reverse mapping...")
        print(gnippam)
        db_file.write(f"local _, ns = ...\nlocal gnippam = {dump_lua(gnippam)}\nns.gnippam = gnippam")

def commit():
    print(f"Commiting new db...")
    os.system(f"cd {git_repo_path} && git config user.email 'aws@aws.com' && git config user.name 'AWS Lambda' && git add * && git commit -m 'Auto Generated DB' && git push")

def lambda_handler(event, ctx):
    global mapping
    mapping = []

    clone_git_repo()
    db = get_mongo_db()

    with ThreadPoolExecutor(max_workers=len(wow_regions)) as executor:
        tasks = [executor.submit(generate_db, db, region) for region in wow_regions]
        
        for future in as_completed(tasks):
            print(f"{future.result()} DB Generated")

    generate_reverse_mapping()
    commit()
    return {
        'statusCode': 200
    }