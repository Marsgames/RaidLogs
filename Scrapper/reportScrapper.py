import requests

from bs4 import BeautifulSoup

urls = {
    "Sepulcher of the First Ones": "https://fr.warcraftlogs.com/zone/reports?zone=29&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
    "Sanctum of Domination": "https://fr.warcraftlogs.com/zone/reports?zone=28&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
    "Castle Nathria": "https://fr.warcraftlogs.com/zone/reports?zone=26&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
}

reportID = ""

queryCN = f"""query {{ 
    reportData {{
        report(code: "{reportID}") {{ 
            rankedCharacters {{
                canonicalID,
                    id,
                    name,
                    server {{
                    name
                }},
                Shriekwing_N: encounterRankings(byBracket: true, encounterID: 2398, compare: Parses, difficulty: 3)
                Huntsman_Altimor_N: encounterRankings(byBracket: true, encounterID: 2418, compare: Parses, difficulty: 3)
                Hungering_Destroyer_N: encounterRankings(byBracket: true, encounterID: 2383, compare: Parses, difficulty: 3)
                Sun_King__s_Salvation_N: encounterRankings(byBracket: true, encounterID: 2402, compare: Parses, difficulty: 3)
                Artificer_Xy__Mox_N: encounterRankings(byBracket: true, encounterID: 2405, compare: Parses, difficulty: 3)
                Lady_Inerva_Darkvein_N: encounterRankings(byBracket: true, encounterID: 2406, compare: Parses, difficulty: 3)
                The_Council_of_Blood_N: encounterRankings(byBracket: true, encounterID: 2412, compare: Parses, difficulty: 3)
                Sludgefist_N: encounterRankings(byBracket: true, encounterID: 2399, compare: Parses, difficulty: 3)
                Stone_Legion_Generals_N: encounterRankings(byBracket: true, encounterID: 2417, compare: Parses, difficulty: 3)
                Sire_Denathrius_N: encounterRankings(byBracket: true, encounterID: 2407, compare: Parses, difficulty: 3)
                Shriekwing_H: encounterRankings(byBracket: true, encounterID: 2398, compare: Parses, difficulty: 4)
                Huntsman_Altimor_H: encounterRankings(byBracket: true, encounterID: 2418, compare: Parses, difficulty: 4)
                Hungering_Destroyer_H: encounterRankings(byBracket: true, encounterID: 2383, compare: Parses, difficulty: 4)
                Sun_King__s_Salvation_H: encounterRankings(byBracket: true, encounterID: 2402, compare: Parses, difficulty: 4)
                Artificer_Xy__Mox_H: encounterRankings(byBracket: true, encounterID: 2405, compare: Parses, difficulty: 4)
                Lady_Inerva_Darkvein_H: encounterRankings(byBracket: true, encounterID: 2406, compare: Parses, difficulty: 4)
                The_Council_of_Blood_H: encounterRankings(byBracket: true, encounterID: 2412, compare: Parses, difficulty: 4)
                Sludgefist_H: encounterRankings(byBracket: true, encounterID: 2399, compare: Parses, difficulty: 4)
                Stone_Legion_Generals_H: encounterRankings(byBracket: true, encounterID: 2417, compare: Parses, difficulty: 4)
                Sire_Denathrius_H: encounterRankings(byBracket: true, encounterID: 2407, compare: Parses, difficulty: 4)
                Shriekwing_M: encounterRankings(byBracket: true, encounterID: 2398, compare: Parses, difficulty: 5)
                Huntsman_Altimor_M: encounterRankings(byBracket: true, encounterID: 2418, compare: Parses, difficulty: 5)
                Hungering_Destroyer_M: encounterRankings(byBracket: true, encounterID: 2383, compare: Parses, difficulty: 5)
                Sun_King__s_Salvation_M: encounterRankings(byBracket: true, encounterID: 2402, compare: Parses, difficulty: 5)
                Artificer_Xy__Mox_M: encounterRankings(byBracket: true, encounterID: 2405, compare: Parses, difficulty: 5)
                Lady_Inerva_Darkvein_M: encounterRankings(byBracket: true, encounterID: 2406, compare: Parses, difficulty: 5)
                The_Council_of_Blood_M: encounterRankings(byBracket: true, encounterID: 2412, compare: Parses, difficulty: 5)
                Sludgefist_M: encounterRankings(byBracket: true, encounterID: 2399, compare: Parses, difficulty: 5)
                Stone_Legion_Generals_M: encounterRankings(byBracket: true, encounterID: 2417, compare: Parses, difficulty: 5)
                Sire_Denathrius_M: encounterRankings(byBracket: true, encounterID: 2407, compare: Parses, difficulty: 5)
            }}
        }}
    }}
}}"""

querySoD = f"""query {{ 
    reportData {{
        report(code: "{reportID}") {{ 
            rankedCharacters {{
                canonicalID,
                    id,
                    name,
                    server {{
                      name
                    }},
                The_Tarragrue_N: encounterRankings(byBracket: true, encounterID: 2423, compare: Parses, difficulty: 3)
                The_Tarragrue_H: encounterRankings(byBracket: true, encounterID: 2423, compare: Parses, difficulty: 4)
                The_Tarragrue_M: encounterRankings(byBracket: true, encounterID: 2423, compare: Parses, difficulty: 5)
                The_Eye_of_the_Jailer_N: encounterRankings(byBracket: true, encounterID: 2433, compare: Parses, difficulty: 3)
                The_Eye_of_the_Jailer_H: encounterRankings(byBracket: true, encounterID: 2433, compare: Parses, difficulty: 4)
                The_Eye_of_the_Jailer_M: encounterRankings(byBracket: true, encounterID: 2433, compare: Parses, difficulty: 5)
                The_Nine_N: encounterRankings(byBracket: true, encounterID: 2429, compare: Parses, difficulty: 3)
                The_Nine_H: encounterRankings(byBracket: true, encounterID: 2429, compare: Parses, difficulty: 4)
                The_Nine_M: encounterRankings(byBracket: true, encounterID: 2429, compare: Parses, difficulty: 5)
                Remnant_of_Ner__zhul_N: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 3)
                Remnant_of_Ner__zhul_H: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 4)
                Remnant_of_Ner__zhul_M: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 5)
                Soulrender_Dormazain_N: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 3)
                Soulrender_Dormazain_H: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 4)
                Soulrender_Dormazain_M: encounterRankings(byBracket: true, encounterID: 2432, compare: Parses, difficulty: 5)
                Painsmith_Raznal_N: encounterRankings(byBracket: true, encounterID: 2430, compare: Parses, difficulty: 3)
                Painsmith_Raznal_H: encounterRankings(byBracket: true, encounterID: 2430, compare: Parses, difficulty: 4)
                Painsmith_Raznal_M: encounterRankings(byBracket: true, encounterID: 2430, compare: Parses, difficulty: 5)
                Guardian_of_the_First_Ones_N: encounterRankings(byBracket: true, encounterID: 2436, compare: Parses, difficulty: 3)
                Guardian_of_the_First_Ones_H: encounterRankings(byBracket: true, encounterID: 2436, compare: Parses, difficulty: 4)
                Guardian_of_the_First_Ones_M: encounterRankings(byBracket: true, encounterID: 2436, compare: Parses, difficulty: 5)
                Fatescribe_Roh____Kalo_N: encounterRankings(byBracket: true, encounterID: 2431, compare: Parses, difficulty: 3)
                Fatescribe_Roh____Kalo_H: encounterRankings(byBracket: true, encounterID: 2431, compare: Parses, difficulty: 4)
                Fatescribe_Roh____Kalo_M: encounterRankings(byBracket: true, encounterID: 2431, compare: Parses, difficulty: 5)
                Kel__Thuzad_N: encounterRankings(byBracket: true, encounterID: 2422, compare: Parses, difficulty: 3)
                Kel__Thuzad_H: encounterRankings(byBracket: true, encounterID: 2422, compare: Parses, difficulty: 4)
                Kel__Thuzad_M: encounterRankings(byBracket: true, encounterID: 2422, compare: Parses, difficulty: 5)
                Sylvnas_Windrunner_N: encounterRankings(byBracket: true, encounterID: 2435, compare: Parses, difficulty: 3)
                Sylvnas_Windrunner_H: encounterRankings(byBracket: true, encounterID: 2435, compare: Parses, difficulty: 4)
                Sylvnas_Windrunner_M: encounterRankings(byBracket: true, encounterID: 2435, compare: Parses, difficulty: 5)

            }}
        }}
    }}
}}"""

querySotFO = f"""query {{ 
    reportData {{
        report(code: "{reportID}") {{ 
            rankedCharacters {{
                canonicalID,
                    id,
                    name,
                    server {{
                    name
                }},
                Vigilant_Guardian_N: encounterRankings(byBracket: true, encounterID: 2512, compare: Parses, difficulty: 3)
                Vigilant_Guardian_H: encounterRankings(byBracket: true, encounterID: 2512, compare: Parses, difficulty: 4)
                Vigilant_Guardian_M: encounterRankings(byBracket: true, encounterID: 2512, compare: Parses, difficulty: 5)
                Dausegne____The_Fallen_Oracle_N: encounterRankings(byBracket: true, encounterID: 2540, compare: Parses, difficulty: 3)
                Dausegne____The_Fallen_Oracle_H: encounterRankings(byBracket: true, encounterID: 2540, compare: Parses, difficulty: 4)
                Dausegne____The_Fallen_Oracle_M: encounterRankings(byBracket: true, encounterID: 2540, compare: Parses, difficulty: 5)
                Artificer_Xy__Mox_N: encounterRankings(byBracket: true, encounterID: 2553, compare: Parses, difficulty: 3)
                Artificer_Xy__Mox_H: encounterRankings(byBracket: true, encounterID: 2553, compare: Parses, difficulty: 4)
                Artificer_Xy__Mox_M: encounterRankings(byBracket: true, encounterID: 2553, compare: Parses, difficulty: 5)
                Prototype_Pantheon_N: encounterRankings(byBracket: true, encounterID: 2544, compare: Parses, difficulty: 3)
                Prototype_Pantheon_H: encounterRankings(byBracket: true, encounterID: 2544, compare: Parses, difficulty: 4)
                Prototype_Pantheon_M: encounterRankings(byBracket: true, encounterID: 2544, compare: Parses, difficulty: 5)
                Skolex____the_Insatiable_Ravener_N: encounterRankings(byBracket: true, encounterID: 2542, compare: Parses, difficulty: 3)
                Skolex____the_Insatiable_Ravener_H: encounterRankings(byBracket: true, encounterID: 2542, compare: Parses, difficulty: 4)
                Skolex____the_Insatiable_Ravener_M: encounterRankings(byBracket: true, encounterID: 2542, compare: Parses, difficulty: 5)
                Halondrus_the_Reclaimer_N: encounterRankings(byBracket: true, encounterID: 2529, compare: Parses, difficulty: 3)
                Halondrus_the_Reclaimer_H: encounterRankings(byBracket: true, encounterID: 2529, compare: Parses, difficulty: 4)
                Halondrus_the_Reclaimer_M: encounterRankings(byBracket: true, encounterID: 2529, compare: Parses, difficulty: 5)
                Lihuvim____Principal_Architect_N: encounterRankings(byBracket: true, encounterID: 2539, compare: Parses, difficulty: 3)
                Lihuvim____Principal_Architect_H: encounterRankings(byBracket: true, encounterID: 2539, compare: Parses, difficulty: 4)
                Lihuvim____Principal_Architect_M: encounterRankings(byBracket: true, encounterID: 2539, compare: Parses, difficulty: 5)
                Anduin_Wrynn_N: encounterRankings(byBracket: true, encounterID: 2546, compare: Parses, difficulty: 3)
                Anduin_Wrynn_H: encounterRankings(byBracket: true, encounterID: 2546, compare: Parses, difficulty: 4)
                Anduin_Wrynn_M: encounterRankings(byBracket: true, encounterID: 2546, compare: Parses, difficulty: 5)
                Lords_of_Dread_N: encounterRankings(byBracket: true, encounterID: 2543, compare: Parses, difficulty: 3)
                Lords_of_Dread_H: encounterRankings(byBracket: true, encounterID: 2543, compare: Parses, difficulty: 4)
                Lords_of_Dread_M: encounterRankings(byBracket: true, encounterID: 2543, compare: Parses, difficulty: 5)
                Rygelon_N: encounterRankings(byBracket: true, encounterID: 2549, compare: Parses, difficulty: 3)
                Rygelon_H: encounterRankings(byBracket: true, encounterID: 2549, compare: Parses, difficulty: 4)
                Rygelon_M: encounterRankings(byBracket: true, encounterID: 2549, compare: Parses, difficulty: 5)
                The_Jailer_N: encounterRankings(byBracket: true, encounterID: 2537, compare: Parses, difficulty: 3)
                The_Jailer_H: encounterRankings(byBracket: true, encounterID: 2537, compare: Parses, difficulty: 4)
                The_Jailer_M: encounterRankings(byBracket: true, encounterID: 2537, compare: Parses, difficulty: 5)
            }}
        }}
    }}
}}"""

for key, value in urls.items():
    links = []
    # find pattern "/reports/xxxxxxxxxxxxxxxx"
    soup = BeautifulSoup(requests.get(value).text, "html.parser")
    for link in soup.find_all("a", href=True):
        if "/reports/" in link["href"]:
            # print what's after "/reports/"
            print(link["href"][9:])
            links.append(link["href"][9:])

    # populate alreadyscraped with file key.txt
    alreadyscraped = []
    with open(f"{key}.txt", "r") as f:
        for line in f:
            alreadyscraped.append(line.strip())
    # remove duplicates
    links = list(set(links))
    # remove already scraped
    links = [x for x in links if x not in alreadyscraped]

    # TODO: Do what you want with links
    # TODO: Execute content of populateDB.py here
    for link in links:
        pass

    # append new links to file
    with open(f"{key}.txt", "a") as f:
        for link in links:
            f.write(link + "\n")
