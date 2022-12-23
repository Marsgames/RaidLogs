import datetime
import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient, UpdateOne
import json

MONGO_USER = os.environ['MONGO_USER']
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']
MONGO_PORT = os.environ['MONGO_PORT']
wcl_report_first_page = int(os.environ['WCL_FIRST_PAGE'])
wcl_report_last_page = int(os.environ['WCL_LAST_PAGE'])
raids = json.loads(os.environ['RAIDS'])
difficulties = json.loads(os.environ['DIFFICULTIES'])

wcl_web_url = "https://www.warcraftlogs.com/zone/reports?zone={}&difficulty={}&page={}"
headers = {
    "Referer" :  "https://www.warcraftlogs.com/"
}
MONGO_CLIENT = None

def connect_mongo():
    global MONGO_CLIENT

    client = MongoClient(
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@149.202.45.54:{MONGO_PORT}/?authMechanism=DEFAULT",
        serverSelectionTimeoutMS=2500
    )
    try:
        # The ping command is cheap and does not require auth.
        client.admin.command("ping")
        MONGO_CLIENT = client.wcl
    except Exception as e:
        print(f"Unable to connect to server:\n\t{e}")

def get_recent_reports(url_template, raid_id, difficulty):
    print(f"Discovering reports for raid {raid_id} difficulty {difficulty} - Page {wcl_report_first_page} to {wcl_report_last_page}")
    reports = []

    for page_id in range(wcl_report_first_page, wcl_report_last_page):
        nb_report = 0
        response = requests.get(url_template.format(raid_id, difficulty, page_id), headers=headers)
        if not response.ok:
            raise Exception(f"[WARN] Call failed ({response.status_code})\n{response.text}\n{url_template.format(raid_id, page_id)}")
        
        soup = BeautifulSoup(response.text, "html.parser")
        for row in soup.find_all("td", { "class" : "description-cell"}):
            link = row.find("a", href=True)
            
            if link and "/reports/" in link["href"]:
                report_id = link["href"].split('/')[-1]
                nb_report += 1
                reports.append(report_id)
            else:
                continue
        
    if nb_report == 0:
        print(f"Early exit empty page - Discovered {len(reports)} reports for raid {raid_id} difficulty {difficulty} - Page {wcl_report_first_page} to {wcl_report_last_page}")

    print(f"Discovered {len(reports)} reports for raid {raid_id} difficulty {difficulty} - Page {wcl_report_first_page} to {wcl_report_last_page}")
    return reports

def upsert_reports(reports):
    print(f"Saving reports discovered infos to MongoDB...")
    requests = []
    for id in reports:
        requests.append(
            UpdateOne({"_id": id}, { "$set": { 'lastSeen': datetime.datetime.now().timestamp() } }, upsert=True)
        )
    
    if len(requests) == 0:
        print("Nothing to store in mongo")
        return
    
    MONGO_CLIENT.reports.bulk_write(requests, ordered=False)
    
def lambda_handler(event, ctx):
    recent_reports = []

    connect_mongo()

    for raid_id in raids:
        for difficulty in difficulties:
            recent_reports.extend(get_recent_reports(wcl_web_url, int(raid_id), int(difficulty)))
    
    recent_reports = [*set(recent_reports)]
    print(f"Total number of reports discovered across all difficulties : {len(recent_reports)}")

    upsert_reports(recent_reports)

    return {'statusCode': 200}