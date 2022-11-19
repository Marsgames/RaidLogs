import boto3
import requests
import json
from datetime import datetime, timedelta

last_auth = datetime.now() - timedelta(hours=2)
auth_token = ""
dynamo = boto3.resource('dynamodb')
wcl_table = dynamo.Table('wcl-statistics')
wcl_token_url = "https://www.warcraftlogs.com/oauth/token"
wcl_token_payload={'grant_type': 'client_credentials'}
sqs_reports_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-discovered-players"
sqs = boto3.client('sqs')
#Bad, should use lambda var but flemme
wcl_token_headers = {
  'Authorization': 'Basic OTdiOWVmODMtOTgwZi00ZTc0LTk1NDktZjNjN2E0MTk0NmU1OlJNem9jeHJOS2RhSmZpSkd2OXZjYVU2WkcwZjNTNjJCcE1rOE9Ueko='
}
wcl_api_url = "https://www.warcraftlogs.com/api/v2/client"
wcl_alias_to_encounter_mapping = {
    "Shriekwing_N" : 2398,
    "Huntsman_Altimor_N" : 2418,
    "Hungering_Destroyer_N" : 2383,
    "Sun_King__s_Salvation_N" : 2402,
    "Artificer_Xy__Mox_N" : 2405,
    "Lady_Inerva_Darkvein_N" : 2406,
    "The_Council_of_Blood_N" : 2412,
    "Sludgefist_N" : 2399,
    "Stone_Legion_Generals_N" : 2417,
    "Sire_Denathrius_N" : 2407,
    "Shriekwing_H" : 2398,
    "Huntsman_Altimor_H" : 2418,
    "Hungering_Destroyer_H" : 2383,
    "Sun_King__s_Salvation_H" : 2402,
    "Artificer_Xy__Mox_H" : 2405,
    "Lady_Inerva_Darkvein_H" : 2406,
    "The_Council_of_Blood_H" : 2412,
    "Sludgefist_H" : 2399,
    "Stone_Legion_Generals_H" : 2417,
    "Sire_Denathrius_H" : 2407,
    "Shriekwing_M" : 2398,
    "Huntsman_Altimor_M" : 2418,
    "Hungering_Destroyer_M" : 2383,
    "Sun_King__s_Salvation_M" : 2402,
    "Artificer_Xy__Mox_M" : 2405,
    "Lady_Inerva_Darkvein_M" : 2406,
    "The_Council_of_Blood_M" : 2412,
    "Sludgefist_M" : 2399,
    "Stone_Legion_Generals_M" : 2417,
    "Sire_Denathrius_M" : 2407,
    "The_Tarragrue_N" : 2423,
    "The_Tarragrue_H" : 2423,
    "The_Tarragrue_M" : 2423,
    "The_Eye_of_the_Jailer_N" : 2433,
    "The_Eye_of_the_Jailer_H" : 2433,
    "The_Eye_of_the_Jailer_M" : 2433,
    "The_Nine_N" : 2429,
    "The_Nine_H" : 2429,
    "The_Nine_M" : 2429,
    "Remnant_of_Ner__zhul_N" : 2432,
    "Remnant_of_Ner__zhul_H" : 2432,
    "Remnant_of_Ner__zhul_M" : 2432,
    "Soulrender_Dormazain_N" : 2432,
    "Soulrender_Dormazain_H" : 2432,
    "Soulrender_Dormazain_M" : 2432,
    "Painsmith_Raznal_N" : 2430,
    "Painsmith_Raznal_H" : 2430,
    "Painsmith_Raznal_M" : 2430,
    "Guardian_of_the_First_Ones_N" : 2436,
    "Guardian_of_the_First_Ones_H" : 2436,
    "Guardian_of_the_First_Ones_M" : 2436,
    "Fatescribe_Roh____Kalo_N" : 2431,
    "Fatescribe_Roh____Kalo_H" : 2431,
    "Fatescribe_Roh____Kalo_M" : 2431,
    "Kel__Thuzad_N" : 2422,
    "Kel__Thuzad_H" : 2422,
    "Kel__Thuzad_M" : 2422,
    "Sylvnas_Windrunner_N" : 2435,
    "Sylvnas_Windrunner_H" : 2435,
    "Sylvnas_Windrunner_M" : 2435,
    "Vigilant_Guardian_N" : 2512,
    "Vigilant_Guardian_H" : 2512,
    "Vigilant_Guardian_M" : 2512,
    "Dausegne____The_Fallen_Oracle_N" : 2540,
    "Dausegne____The_Fallen_Oracle_H" : 2540,
    "Dausegne____The_Fallen_Oracle_M" : 2540,
    "Artificer_Xy__Mox_N" : 2553,
    "Artificer_Xy__Mox_H" : 2553,
    "Artificer_Xy__Mox_M" : 2553,
    "Prototype_Pantheon_N" : 2544,
    "Prototype_Pantheon_H" : 2544,
    "Prototype_Pantheon_M" : 2544,
    "Skolex____the_Insatiable_Ravener_N" : 2542,
    "Skolex____the_Insatiable_Ravener_H" : 2542,
    "Skolex____the_Insatiable_Ravener_M" : 2542,
    "Halondrus_the_Reclaimer_N" : 2529,
    "Halondrus_the_Reclaimer_H" : 2529,
    "Halondrus_the_Reclaimer_M" : 2529,
    "Lihuvim____Principal_Architect_N" : 2539,
    "Lihuvim____Principal_Architect_H" : 2539,
    "Lihuvim____Principal_Architect_M" : 2539,
    "Anduin_Wrynn_N" : 2546,
    "Anduin_Wrynn_H" : 2546,
    "Anduin_Wrynn_M" : 2546,
    "Lords_of_Dread_N" : 2543,
    "Lords_of_Dread_H" : 2543,
    "Lords_of_Dread_M" : 2543,
    "Rygelon_N" : 2549,
    "Rygelon_H" : 2549,
    "Rygelon_M" : 2549,
    "The_Jailer_N" : 2537,
    "The_Jailer_H" : 2537,
    "The_Jailer_M" : 2537
}
wcl_queries = {
    #Nathria
    26: "{{\"query\": \"query {{  \
    characterData {{ \
        character(id: {}) {{  \
                    name, \
                    server {{ \
                    name \
                }}, \
                Shriekwing_N: encounterRankings(byBracket: true, encounterID: 2398, compare: Parses, difficulty: 3) \
                Huntsman_Altimor_N: encounterRankings(byBracket: true, encounterID: 2418, compare: Parses, difficulty: 3) \
                Hungering_Destroyer_N: encounterRankings(byBracket: true, encounterID: 2383, compare: Parses, difficulty: 3) \
                Sun_King__s_Salvation_N: encounterRankings(byBracket: true, encounterID: 2402, compare: Parses, difficulty: 3) \
                Artificer_Xy__Mox_N: encounterRankings(byBracket: true, encounterID: 2405, compare: Parses, difficulty: 3) \
                Lady_Inerva_Darkvein_N: encounterRankings(byBracket: true, encounterID: 2406, compare: Parses, difficulty: 3) \
                The_Council_of_Blood_N: encounterRankings(byBracket: true, encounterID: 2412, compare: Parses, difficulty: 3) \
                Sludgefist_N: encounterRankings(byBracket: true, encounterID: 2399, compare: Parses, difficulty: 3) \
                Stone_Legion_Generals_N: encounterRankings(byBracket: true, encounterID: 2417, compare: Parses, difficulty: 3) \
                Sire_Denathrius_N: encounterRankings(byBracket: true, encounterID: 2407, compare: Parses, difficulty: 3) \
                Shriekwing_H: encounterRankings(byBracket: true, encounterID: 2398, compare: Parses, difficulty: 4) \
                Huntsman_Altimor_H: encounterRankings(byBracket: true, encounterID: 2418, compare: Parses, difficulty: 4) \
                Hungering_Destroyer_H: encounterRankings(byBracket: true, encounterID: 2383, compare: Parses, difficulty: 4) \
                Sun_King__s_Salvation_H: encounterRankings(byBracket: true, encounterID: 2402, compare: Parses, difficulty: 4) \
                Artificer_Xy__Mox_H: encounterRankings(byBracket: true, encounterID: 2405, compare: Parses, difficulty: 4) \
                Lady_Inerva_Darkvein_H: encounterRankings(byBracket: true, encounterID: 2406, compare: Parses, difficulty: 4) \
                The_Council_of_Blood_H: encounterRankings(byBracket: true, encounterID: 2412, compare: Parses, difficulty: 4) \
                Sludgefist_H: encounterRankings(byBracket: true, encounterID: 2399, compare: Parses, difficulty: 4) \
                Stone_Legion_Generals_H: encounterRankings(byBracket: true, encounterID: 2417, compare: Parses, difficulty: 4) \
                Sire_Denathrius_H: encounterRankings(byBracket: true, encounterID: 2407, compare: Parses, difficulty: 4) \
                Shriekwing_M: encounterRankings(byBracket: true, encounterID: 2398, compare: Parses, difficulty: 5) \
                Huntsman_Altimor_M: encounterRankings(byBracket: true, encounterID: 2418, compare: Parses, difficulty: 5) \
                Hungering_Destroyer_M: encounterRankings(byBracket: true, encounterID: 2383, compare: Parses, difficulty: 5) \
                Sun_King__s_Salvation_M: encounterRankings(byBracket: true, encounterID: 2402, compare: Parses, difficulty: 5) \
                Artificer_Xy__Mox_M: encounterRankings(byBracket: true, encounterID: 2405, compare: Parses, difficulty: 5) \
                Lady_Inerva_Darkvein_M: encounterRankings(byBracket: true, encounterID: 2406, compare: Parses, difficulty: 5) \
                The_Council_of_Blood_M: encounterRankings(byBracket: true, encounterID: 2412, compare: Parses, difficulty: 5) \
                Sludgefist_M: encounterRankings(byBracket: true, encounterID: 2399, compare: Parses, difficulty: 5) \
                Stone_Legion_Generals_M: encounterRankings(byBracket: true, encounterID: 2417, compare: Parses, difficulty: 5) \
                Sire_Denathrius_M: encounterRankings(byBracket: true, encounterID: 2407, compare: Parses, difficulty: 5) \
        }} \
    }} \
}}\"}}",
#sanctum
28: "{{\"query\": \"query {{  \
    characterData {{ \
        character(id: {}) {{ \
                    name, \
                    server {{ \
                      name \
                    }}, \
                The_Tarragrue_N: encounterRankings(byBracket: true, encounterID: 2423, compare: Parses, difficulty: 3) \
                The_Tarragrue_H: encounterRankings(byBracket: true, encounterID: 2423, compare: Parses, difficulty: 4) \
                The_Tarragrue_M: encounterRankings(byBracket: true, encounterID: 2423, compare: Parses, difficulty: 5) \
                The_Eye_of_the_Jailer_N: encounterRankings(byBracket: true, encounterID: 2433, compare: Parses, difficulty: 3) \
                The_Eye_of_the_Jailer_H: encounterRankings(byBracket: true, encounterID: 2433, compare: Parses, difficulty: 4) \
                The_Eye_of_the_Jailer_M: encounterRankings(byBracket: true, encounterID: 2433, compare: Parses, difficulty: 5) \
                The_Nine_N: encounterRankings(byBracket: true, encounterID: 2429, compare: Parses, difficulty: 3) \
                The_Nine_H: encounterRankings(byBracket: true, encounterID: 2429, compare: Parses, difficulty: 4) \
                The_Nine_M: encounterRankings(byBracket: true, encounterID: 2429, compare: Parses, difficulty: 5) \
                Remnant_of_Ner__zhul_N: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 3) \
                Remnant_of_Ner__zhul_H: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 4) \
                Remnant_of_Ner__zhul_M: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 5) \
                Soulrender_Dormazain_N: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 3) \
                Soulrender_Dormazain_H: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 4) \
                Soulrender_Dormazain_M: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 5) \
                Painsmith_Raznal_N: encounterRankings(byBracket: true, encounterID: 2430, compare: Parses, difficulty: 3) \
                Painsmith_Raznal_H: encounterRankings(byBracket: true, encounterID: 2430, compare: Parses, difficulty: 4) \
                Painsmith_Raznal_M: encounterRankings(byBracket: true, encounterID: 2430, compare: Parses, difficulty: 5) \
                Guardian_of_the_First_Ones_N: encounterRankings(byBracket: true, encounterID: 2436, compare: Parses, difficulty: 3) \
                Guardian_of_the_First_Ones_H: encounterRankings(byBracket: true, encounterID: 2436, compare: Parses, difficulty: 4) \
                Guardian_of_the_First_Ones_M: encounterRankings(byBracket: true, encounterID: 2436, compare: Parses, difficulty: 5) \
                Fatescribe_Roh____Kalo_N: encounterRankings(byBracket: true, encounterID: 2431, compare: Parses, difficulty: 3) \
                Fatescribe_Roh____Kalo_H: encounterRankings(byBracket: true, encounterID: 2431, compare: Parses, difficulty: 4) \
                Fatescribe_Roh____Kalo_M: encounterRankings(byBracket: true, encounterID: 2431, compare: Parses, difficulty: 5) \
                Kel__Thuzad_N: encounterRankings(byBracket: true, encounterID: 2422, compare: Parses, difficulty: 3) \
                Kel__Thuzad_H: encounterRankings(byBracket: true, encounterID: 2422, compare: Parses, difficulty: 4) \
                Kel__Thuzad_M: encounterRankings(byBracket: true, encounterID: 2422, compare: Parses, difficulty: 5) \
                Sylvnas_Windrunner_N: encounterRankings(byBracket: true, encounterID: 2435, compare: Parses, difficulty: 3) \
                Sylvnas_Windrunner_H: encounterRankings(byBracket: true, encounterID: 2435, compare: Parses, difficulty: 4) \
                Sylvnas_Windrunner_M: encounterRankings(byBracket: true, encounterID: 2435, compare: Parses, difficulty: 5) \
        }} \
    }} \
}}\"}}",
#Sepulcher
29: "{{\"query\": \"query {{ \
    characterData {{ \
        character(id: {}) {{ \
                    name, \
                    server {{ \
                    name \
                }}, \
                Vigilant_Guardian_N: encounterRankings(byBracket: true, encounterID: 2512, compare: Parses, difficulty: 3) \
                Vigilant_Guardian_H: encounterRankings(byBracket: true, encounterID: 2512, compare: Parses, difficulty: 4) \
                Vigilant_Guardian_M: encounterRankings(byBracket: true, encounterID: 2512, compare: Parses, difficulty: 5) \
                Dausegne____The_Fallen_Oracle_N: encounterRankings(byBracket: true, encounterID: 2540, compare: Parses, difficulty: 3) \
                Dausegne____The_Fallen_Oracle_H: encounterRankings(byBracket: true, encounterID: 2540, compare: Parses, difficulty: 4) \
                Dausegne____The_Fallen_Oracle_M: encounterRankings(byBracket: true, encounterID: 2540, compare: Parses, difficulty: 5) \
                Artificer_Xy__Mox_N: encounterRankings(byBracket: true, encounterID: 2553, compare: Parses, difficulty: 3) \
                Artificer_Xy__Mox_H: encounterRankings(byBracket: true, encounterID: 2553, compare: Parses, difficulty: 4) \
                Artificer_Xy__Mox_M: encounterRankings(byBracket: true, encounterID: 2553, compare: Parses, difficulty: 5) \
                Prototype_Pantheon_N: encounterRankings(byBracket: true, encounterID: 2544, compare: Parses, difficulty: 3) \
                Prototype_Pantheon_H: encounterRankings(byBracket: true, encounterID: 2544, compare: Parses, difficulty: 4) \
                Prototype_Pantheon_M: encounterRankings(byBracket: true, encounterID: 2544, compare: Parses, difficulty: 5) \
                Skolex____the_Insatiable_Ravener_N: encounterRankings(byBracket: true, encounterID: 2542, compare: Parses, difficulty: 3) \
                Skolex____the_Insatiable_Ravener_H: encounterRankings(byBracket: true, encounterID: 2542, compare: Parses, difficulty: 4) \
                Skolex____the_Insatiable_Ravener_M: encounterRankings(byBracket: true, encounterID: 2542, compare: Parses, difficulty: 5) \
                Halondrus_the_Reclaimer_N: encounterRankings(byBracket: true, encounterID: 2529, compare: Parses, difficulty: 3) \
                Halondrus_the_Reclaimer_H: encounterRankings(byBracket: true, encounterID: 2529, compare: Parses, difficulty: 4) \
                Halondrus_the_Reclaimer_M: encounterRankings(byBracket: true, encounterID: 2529, compare: Parses, difficulty: 5) \
                Lihuvim____Principal_Architect_N: encounterRankings(byBracket: true, encounterID: 2539, compare: Parses, difficulty: 3) \
                Lihuvim____Principal_Architect_H: encounterRankings(byBracket: true, encounterID: 2539, compare: Parses, difficulty: 4) \
                Lihuvim____Principal_Architect_M: encounterRankings(byBracket: true, encounterID: 2539, compare: Parses, difficulty: 5) \
                Anduin_Wrynn_N: encounterRankings(byBracket: true, encounterID: 2546, compare: Parses, difficulty: 3) \
                Anduin_Wrynn_H: encounterRankings(byBracket: true, encounterID: 2546, compare: Parses, difficulty: 4) \
                Anduin_Wrynn_M: encounterRankings(byBracket: true, encounterID: 2546, compare: Parses, difficulty: 5) \
                Lords_of_Dread_N: encounterRankings(byBracket: true, encounterID: 2543, compare: Parses, difficulty: 3) \
                Lords_of_Dread_H: encounterRankings(byBracket: true, encounterID: 2543, compare: Parses, difficulty: 4) \
                Lords_of_Dread_M: encounterRankings(byBracket: true, encounterID: 2543, compare: Parses, difficulty: 5) \
                Rygelon_N: encounterRankings(byBracket: true, encounterID: 2549, compare: Parses, difficulty: 3) \
                Rygelon_H: encounterRankings(byBracket: true, encounterID: 2549, compare: Parses, difficulty: 4) \
                Rygelon_M: encounterRankings(byBracket: true, encounterID: 2549, compare: Parses, difficulty: 5) \
                The_Jailer_N: encounterRankings(byBracket: true, encounterID: 2537, compare: Parses, difficulty: 3) \
                The_Jailer_H: encounterRankings(byBracket: true, encounterID: 2537, compare: Parses, difficulty: 4) \
                The_Jailer_M: encounterRankings(byBracket: true, encounterID: 2537, compare: Parses, difficulty: 5) \
        }} \
    }} \
}}\"}}"
}

class Player:
    def __init__(self, player_data, id, rank):
        self.load_data_from_json(player_data, id, rank)
    
    def append_raids_data(self, player_data, rank):
        player_data.pop("name", None)
        player_data.pop("server", None)

        for key, bossData in player_data.items():
            self.raids.append({
                "rank": rank,
                "encounter": wcl_alias_to_encounter_mapping[key],
                "tag": key,
                "difficulty": bossData["difficulty"],
                "zone": bossData["zone"],
                "metric": bossData["metric"],
                "averagePerformance": int(bossData["averagePerformance"] or 0),
                "bestPerformance": int(max(rank["rankPercent"] for rank in bossData["ranks"]) if len(bossData["ranks"]) > 0 else 0),
                "totalKills": bossData["totalKills"]
            })

    def load_data_from_json(self, player_data, id, rank):
        self.name = player_data.pop("name")
        self.id = id
        self.server = player_data.pop("server")["name"]
        self.raids = []

        self.append_raids_data(player_data, rank) 

def get_auth_token():
    global last_auth
    last_auth = datetime.now()

    print(f"Auth expired, renewing")
    response = requests.request("POST", wcl_token_url, headers=wcl_token_headers, data=wcl_token_payload)
    return response.json()["access_token"]

def get_players_stats_for_player(playerRankMsg, players):
    global auth_token
    playerId = playerRankMsg["id"]
    if datetime.now() - timedelta(hours=1) > last_auth:
        auth_token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    for raidId, rank in playerRankMsg["raidsRank"].items():
        query = wcl_queries[int(raidId)]

        response = requests.request("POST", wcl_api_url, headers=headers, data=query.format(playerId))
        
        player_data = response.json()["data"]["characterData"]["character"]
        
        if playerId in players:
            players[playerId].append_raids_data(player_data, rank)
        else:
            players[playerId] = Player(player_data, playerId, rank)
    return players

def put_players(players):
    print(f"Saving {len(players)} players to DynamoDB")
    print([player.__dict__ for player in players.values()])
    for player in players.values():
        wcl_table.put_item(Item=player.__dict__)
    #Limit batching, because in free tier too fast it reach DynamoDB limit
    #with wcl_table.batch_writer() as batch:
        #for player in players.values():
            #batch.put_item(Item=player.__dict__)

def lambda_handler(event, ctx):
    print(f"Starting with {len(event['Records'])} new messages")
    players = {}
    for record in event['Records']:
        playerRankMsg = json.loads(record["body"])
        players = get_players_stats_for_player(playerRankMsg, players)
        sqs.delete_message(
            QueueUrl=sqs_reports_queue,
            ReceiptHandle=record["receiptHandle"]
        )
    
    put_players(players)
    return {
        'statusCode': 200
    }