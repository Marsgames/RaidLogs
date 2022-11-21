import os
import decimal
from pymongo import MongoClient

git_repo_url = "https://{0}@github.com/Marsgames/WarLogs.git"

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

def get_all_players(db):
    print(f"Retrieving all player from MongoDB")
    players = list(db.players.find({}))
    
    print(f"Found {len(players)} players")

    return players

def clone_git_repo():
    print(f"Cloning git repo...")
    os.system(f"git clone {git_repo_url.format(os.environ['GIT_TOKEN'])} /tmp/WarLogs")

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

def transform_player_data(player):
    tmp_player_data = {}

    for raid in player["raids"].values():
        if raid["zone"] not in tmp_player_data:
            tmp_player_data[raid["zone"]] = {}
        
        if raid["encounter"] not in tmp_player_data[raid["zone"]]:
            tmp_player_data[raid["zone"]][raid["encounter"]] = {}
        
        tmp_player_data[raid["zone"]][raid["encounter"]][raid["difficulty"]] = {
            "rank": raid["rank"],
            "metric": raid["metric"],
            "best": raid["bestPerformance"],
            "avg": raid["averagePerformance"],
            "count": raid["totalKills"]
        }
    
    return tmp_player_data

def generate_db(players):
    db_file = open("/tmp/WarLogs/db/aws-test.lua", "w")
    
    tmp_db = {}
    for player in players: 
        transformed_data = transform_player_data(player)

        if player["server"] not in tmp_db:
            tmp_db[player["server"]] = {}
        
        tmp_db[player["server"]][player["name"]] = transformed_data
    
    str_lua = dump_lua(tmp_db)
    str_base = "local addonName, ns = ... \nlocal db = "
    db_file.write(str_base + str_lua + "\nns.db.char = db")
    db_file.close()

def commit():
    print(f"Commiting new db...")
    os.system(f"cd /tmp/WarLogs && git config user.email 'aws@aws.com' && git config user.name 'AWS Lambda' && git add * && git commit -m 'Auto Generated DB' && git push")

def lambda_handler(event, ctx):
    clone_git_repo()
    db = get_mongo_db()
    players = get_all_players(db)
    generate_db(players)
    commit()
    return {
        'statusCode': 200
    }