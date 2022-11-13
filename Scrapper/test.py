import requests

clientID = "YOUR_CLIENT_ID"
secret = "YOUR_SECRET"

autorisationURI = "https://www.warcraftlogs.com/oauth/authorize"
tokenURI = "https://www.warcraftlogs.com/oauth/token"
baseURL = "https://www.warcraftlogs.com/api/v2/client"

regionsID = {"US": 1, "EU": 2, "KR": 3, "TW": 4, "CN": 5}
euServers = [
    "aerie-peak",
    "agamaggan",
    "aggramar",
    "ahnqiraj",
    "alakir",
    "alonsus",
    "anachronos",
    "arathor",
    "argent-dawn",
    "aszune",
    "auchindoun",
    "azjolnerub",
    "azuremyst",
    "balnazzar",
    "blades-edge",
    "bladefist",
    "bloodfeather",
    "bloodhoof",
    "bloodscalp",
    "boulderfist",
    "bronze-dragonflight",
    "bronzebeard",
    "burning-blade",
    "burning-legion",
    "burning-steppes",
    "chamber-of-aspects",
    "chromaggus",
    "crushridge",
    "daggerspine",
    "darkmoon-faire",
    "darksorrow",
    "darkspear",
    "deathwing",
    "defias-brotherhood",
    "dentarg",
    "doomhammer",
    "draenor",
    "dragonblight",
    "dragonmaw",
    "drakthul",
    "dunemaul",
    "earthen-ring",
    "emerald-dream",
    "emeriss",
    "eonar",
    "executus",
    "frostmane",
    "frostwhisper",
    "genjuros",
    "ghostlands",
    "grim-batol",
    "hakkar",
    "haomarush",
    "hellfire",
    "hellscream",
    "jaedenar",
    "karazhan",
    "kazzak",
    "khadgar",
    "kilrogg",
    "korgall",
    "kul-tiras",
    "laughing-skull",
    "lightbringer",
    "lightnings-blade",
    "magtheridon",
    "mazrigos",
    "moonglade",
    "nagrand",
    "neptulon",
    "nordrassil",
    "outland",
    "quelthalas",
    "ragnaros",
    "ravencrest",
    "ravenholdt",
    "runetotem",
    "saurfang",
    "scarshield-legion",
    "shadowsong",
    "shattered-halls",
    "shattered-hand",
    "silvermoon",
    "skullcrusher",
    "spinebreaker",
    "sporeggar",
    "steamwheedle-cartel",
    "stormrage",
    "stormreaver",
    "stormscale",
    "sunstrider",
    "sylvanas",
    "talnivarr",
    "tarren-mill",
    "terenas",
    "terokkar",
    "the-maelstrom",
    "the-shatar",
    "the-venture-co",
    "thunderhorn",
    "trollbane",
    "turalyon",
    "twilights-hammer",
    "twisting-nether",
    "vashj",
    "veknilash",
    "wildhammer",
    "xavius",
    "zenedar",
    "arakarahm",
    "arathi",
    "archimonde",
    "chants-éternels",
    "chogall",
    "confrérie-du-thorium",
    "conseil-des-ombres",
    "culte-de-la-rive-noire",
    "dalaran",
    "drekthar",
    "eitrigg",
    "eldrethalas",
    "elune",
    "garona",
    "hyjal",
    "illidan",
    "kaelthas",
    "khaz-modan",
    "kirin-tor",
    "krasus",
    "la-croisade-écarlate",
    "les-clairvoyants",
    "les-sentinelles",
    "marécage-de-zangar",
    "medivh",
    "naxxramas",
    "zzzzz",
    "rashgarroth",
    "sargeras",
    "sinstralis",
    "suramar",
    "temple-noir",
    "throkferoth",
    "uldaman",
    "varimathras",
    "voljin",
    "ysondre",
    "aegwynn",
    "alexstrasza",
    "alleria",
    "amanthul",
    "ambossar",
    "anetheron",
    "antonidas",
    "anubarak",
    "area-52",
    "arthas",
    "arygos",
    "azshara",
    "baelgun",
    "blackhand",
    "blackmoore",
    "blackrock",
    "blutkessel",
    "dalvengyr",
    "das-konsortium",
    "das-syndikat",
    "der-abyssische-rat",
    "der-mithrilorden",
    "der-rat-von-dalaran",
    "destromath",
    "dethecus",
    "die-aldor",
    "die-arguswacht",
    "die-nachtwache",
    "die-silberne-hand",
    "die-todeskrallen",
    "die-ewige-wacht",
    "dun-morogh",
    "durotan",
    "echsenkessel",
    "eredar",
    "festung-der-stürme",
    "forscherliga",
    "frostmourne",
    "frostwolf",
    "garrosh",
    "gilneas",
    "gorgonnash",
    "guldan",
    "kargath",
    "kelthuzad",
    "khazgoroth",
    "kiljaeden",
    "kragjin",
    "kult-der-verdammten",
    "lordaeron",
    "lothar",
    "madmortem",
    "malganis",
    "malfurion",
    "malorne",
    "malygos",
    "mannoroth",
    "mugthol",
    "nathrezim",
    "nazjatar",
    "nefarian",
    "nerathor",
    "nethersturm",
    "norgannon",
    "nozdormu",
    "onyxia",
    "perenolde",
    "proudmoore",
    "rajaxx",
    "rexxar",
    "senjin",
    "shattrath",
    "taerar",
    "teldrassil",
    "terrordar",
    "theradras",
    "thrall",
    "tichondrius",
    "tirion",
    "todeswache",
    "ulduar",
    "ungoro",
    "veklor",
    "wrathbringer",
    "ysera",
    "zirkel-des-cenarius",
    "zuluhed",
    "nemesis",
    "pozzo-delleternità",
    "aggra-português",
    "azuregos",
    "borean-tundra",
    "eversong",
    "galakrond",
    "goldrinn",
    "gordunni",
    "grom",
    "fordragon",
    "lich-king",
    "booty-bay",
    "deepholm",
    "razuvious",
    "howling-fjord",
    "soulflayer",
    "greymane",
    "deathguard",
    "thermaplugg",
    "deathweaver",
    "blackscar",
    "ashenvale",
    "cthun",
    "colinas-pardas",
    "dun-modr",
    "exodar",
    "los-errantes",
    "minahonda",
    "sanguino",
    "shendralar",
    "tyrande",
    "uldum",
    "zuljin",
    "nerzhul",
]
shadowlandsZones = [
    {"name": "Sepulcher of the First Ones", "id": 29},
    {"name": "Sanctum of Domination", "id": 28},
    {"name": "Castle Nathria", "id": 26},
]
encounters = {
    "Sepulcher of the First Ones": [
        {"name": "Vigilant Guardian", "id": 2512},
        {"name": "Dausegne, the Fallen Oracle", "id": 2540},
        {"name": "Artificer Xy'mox", "id": 2553},
        {"name": "Prototype Pantheon", "id": 2544},
        {"name": "Skolex, the Insatiable Ravener", "id": 2542},
        {"name": "Halondrus the Reclaimer", "id": 2529},
        {"name": "Lihuvim, Principal Architect", "id": 2539},
        {"name": "Anduin Wrynn", "id": 2546},
        {"name": "Lords of Dread", "id": 2543},
        {"name": "Rygelon", "id": 2549},
        {"name": "The Jailer", "id": 2537},
    ],
    "Sanctum of Domination": [
        {"name": "The Tarragrue", "id": 2423},
        {"name": "The Eye of the Jailer", "id": 2433},
        {"name": "The Nine", "id": 2429},
        {"name": "Remnant of Ner'zhul", "id": 2432},
        {"name": "Soulrender Dormazain", "id": 2434},
        {"name": "Painsmith Raznal", "id": 2430},
        {"name": "Guardian of the First Ones", "id": 2436},
        {"name": "Fatescribe Roh-Kalo", "id": 2431},
        {"name": "Kel'Thuzad", "id": 2422},
        {"name": "Sylvanas Windrunner", "id": 2435},
    ],
    "Castle Nathria": [
        {"name": "Shriekwing", "id": 2398},
        {"name": "Huntsman Altimor", "id": 2418},
        {"name": "Hungering Destroyer", "id": 2383},
        {"name": "Sun King's Salvation", "id": 2402},
        {"name": "Artificer Xy'mox", "id": 2405},
        {"name": "Lady Inerva Darkvein", "id": 2406},
        {"name": "The Council of Blood", "id": 2412},
        {"name": "Sludgefist", "id": 2399},
        {"name": "Stone Legion Generals", "id": 2417},
        {"name": "Sire Denathrius", "id": 2407},
    ],
}


# Get stats for Niisha on Shriekwing :
"""
query {
	characterData {
		character(name: "Niisha", serverSlug: "temple-noir", serverRegion: "EU") {
			encounterRankings(encounterID: 2398, difficulty: 4, byBracket: true, compare: Parses) {
		}
	}
}
"""

# Get all servers
"""
query {
	worldData {
		regions {
			servers(limit: 100) {
				current_page,
				has_more_pages,
				last_page,
				data {
					name,
					slug,
					region {
						compactName,
						name,
						slug,
						id
					}
				}
			}
		}
	}
}
"""


def GetAllZones(token: str) -> list:
    headers = {"Authorization": f"Bearer {token}"}
    query = """
    query {
        worldData {
	        expansions {
                name,
    			zones {
			        name,
    			    id
    		    }
	        }
   	    }
    }
    """

    r = requests.post(baseURL, headers=headers, json={"query": query})
    return r.json()


def GetEncounters(token: str, zoneID: int) -> list:
    headers = {"Authorization": f"Bearer {token}"}
    query = f"""
    query {{
        worldData {{
            zone(id: {zoneID})
            {{
                name
                encounters {{
                    name
                    id
                }}
            }}
        }}
    }}
    """

    r = requests.post(baseURL, headers=headers, json={"query": query})
    return r.json()


def GetDatas(token: str, player: str, realm: str):
    headers = {"Authorization": f"Bearer {token}"}
    for zone in shadowlandsZones:
        for encounter in encounters[zone["name"]]:
            try:
                query = f"""
                query {{
                    characterData {{
                        character(name: "{player}", serverSlug: "{realm}", serverRegion: "EU") {{
                            encounterRankings(encounterID: {encounter["id"]}, difficulty: 3, byBracket: true, compare: Parses)
                        }}
                    }}
                }}
                """
                # print(
                #     f"----- query for {player} on {realm} for {encounter['name']} -----\n{query}"
                # )

                r = requests.post(baseURL, headers=headers, json={"query": query})
                # print(r.json())
                firstRankPercent = r.json()["data"]["characterData"]["character"][
                    "encounterRankings"
                ]["ranks"][0]["rankPercent"]
                encName = encounter["name"]
                print(f"boss : {encName} - {firstRankPercent} - N")
            except Exception as e:
                print(f"Unable to get data for : {encounter}\n{e}")
                pass
        print("")


def RequestToken() -> str:
    data = {
        "grant_type": "client_credentials",
        "client_id": clientID,
        "client_secret": secret,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    r = requests.post(tokenURI, data=data, headers=headers)
    return r.json()["access_token"]
    # print(f"response : {r.json()}")


def GetAllCharacters(token: str) -> list:
    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(baseURL, headers=headers)
    return r.json()


if __name__ == "__main__":
    access_token = RequestToken()

    # print(GetAllZones(access_token))
    # for zone in shadowlandsZones:
    #     print(f"{zone} : {GetEncounters(access_token, shadowlandsZones[zone])}")
    GetDatas(access_token, "Niisha", "temple-noir")
