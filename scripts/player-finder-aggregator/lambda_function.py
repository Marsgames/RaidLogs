import boto3
import json
import os
from pymongo import MongoClient

sqs = boto3.client('sqs')

sqs_max_batch_size = 10
sqs_player_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-discovered-players"

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

def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def send_discovered_players_in_queue(players):
    print(f'Sending player\'s in queue...')
    batch = []
    idx = 0
    for player in players:
        idx+=1
        if len(batch) == sqs_max_batch_size:
            sqs.send_message_batch(QueueUrl=sqs_player_queue, Entries=batch)
            batch = []
        
        batch.append({"Id": str(player["_id"]), "MessageBody":json.dumps({ "id" : player["_id"], "raids": player["raidsToScrap"]})})

    print(f'{idx} Players sent in queue')

def get_players_mongo(db):
    return db.discovers.find({}, batch_size=1000)

def drop_all_players_discovered_mongo(db):
    print(f'Deleting all players discovered in MongoDB discovers collection')
    return db.discovers.delete_many({})

def lambda_handler(event, ctx):
    db = get_mongo_db()
    players = get_players_mongo(db)
    send_discovered_players_in_queue(players)
    drop_all_players_discovered_mongo(db)

    return { 'statusCode': 200 }