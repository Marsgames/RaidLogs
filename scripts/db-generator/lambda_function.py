import os
import decimal
from pymongo import MongoClient

git_repo_url = "https://{0}@github.com/Marsgames/WarLogs.git"
git_repo_path = "/tmp/WarLogs"

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

def get_all_players_cursor(db):
    print(f"Retrieving all player from MongoDB")
    cursor = db.players.find(batch_size=1000)
    print(f"Cursor generated")
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

def transform_player_data_ugly(player):
    tmp_player_data = []
    for raid in player["raids"].values():
        tmp_player_data.append(f"{raid['encounter']}:{raid['difficulty']}:{raid['rank']}:{raid['metric']}:{raid['bestPerformance']}:{raid['averagePerformance']}:{raid['totalKills']}")
    
    return tmp_player_data

def generate_db(cursor):
    with open(f"{git_repo_path}/db/aws-test2.lua", "w") as db_file:
        tmp_db = {}
        idx = 0
        for player in cursor: 
            if idx % 1000 == 0: 
                print(f"Processed {idx} players")
            transformed_data = transform_player_data_ugly(player)

            if player["server"] not in tmp_db:
                tmp_db[player["server"]] = {}
            
            tmp_db[player["server"]][player["name"]] = transformed_data
            idx += 1

        str_lua = dump_lua(tmp_db)
        str_base = "local addonName, ns = ... \nlocal db = "
        db_file.write(str_base + str_lua + "\nns.db.char = db")

def commit():
    print(f"Commiting new db...")
    os.system(f"cd {git_repo_path} && git config user.email 'aws@aws.com' && git config user.name 'AWS Lambda' && git add * && git commit -m 'Auto Generated DB' && git push")

def get_players_slice(db, offset, limit):
    print(f"Retrieving all player from MongoDB")
    cursor = db.players.find().skip(offset).limit(limit)
    print(f"Cursor generated")
    return cursor

def lambda_handler(event, ctx):
    clone_git_repo()
    db = get_mongo_db()
    #tmp_db = {}

    cursor = get_all_players_cursor(db)
    #with ThreadPoolExecutor(max_workers=2) as executor:
        #db_thread_a = executor.submit(load_players, get_players_slice(db, 0, 1000), tmp_db, 1)
        #db_thread_b = executor.submit(load_players, get_players_slice(db, 1000, 2000), tmp_db, 2)
        #db_thread_c = executor.submit(load_players, get_players_slice(db, 2000, 3000), tmp_db, 3)
        #db_thread_d = executor.submit(load_players, get_players_slice(db, 3000, 4000), tmp_db, 4)
        #db_thread_e = executor.submit(load_players, get_players_slice(db, 4000, 5000), tmp_db, 5)
        
    #db_thread_a.result()
    #db_thread_b.result()
    #db_thread_c.result()
    #db_thread_d.result()
    #db_thread_e.result()

    #print(f"Total retrieved players {len(tmp_db)}")
    generate_db(cursor)
    commit()
    return {
        'statusCode': 200
    }