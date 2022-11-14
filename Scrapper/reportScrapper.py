import requests

from bs4 import BeautifulSoup

urls = {
    "Sepulcher of the First Ones": "https://fr.warcraftlogs.com/zone/reports?zone=29&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
    "Sanctum of Domination": "https://fr.warcraftlogs.com/zone/reports?zone=28&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
    "Castle Nathria": "https://fr.warcraftlogs.com/zone/reports?zone=26&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
}

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
    for link in links:
        pass

    # append new links to file
    with open(f"{key}.txt", "a") as f:
        for link in links:
            f.write(link + "\n")Ò