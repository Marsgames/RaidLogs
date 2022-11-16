import boto3
import requests
import json
from bs4 import BeautifulSoup

sqs_max_batch_size = 10
sqs_last_report_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-last-report"
sqs_reports_queue = "https://sqs.us-east-1.amazonaws.com/697133125351/wcl-reports"
sqs = boto3.client('sqs')
dynamo = boto3.client('dynamodb')

urls = {
    "SepulcherOfTheFirstOnes": 
"https://www.warcraftlogs.com/zone/reports?zone=29&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
    "SanctumOfDomination": 
"https://www.warcraftlogs.com/zone/reports?zone=28&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
    "CastleNathria": 
"https://www.warcraftlogs.com/zone/reports?zone=26&boss=0&difficulty=0&class=Any&spec=Any&keystone=0&kills=0&duration=0",
}

def get_last_reports_id():
    data = dynamo.scan(
        TableName='wclLastReportsId'
    )
    print(data)

    if "Items" in data:
        return {item['zone']['S']:item['reportId']['S'] for item in data["Items"]}

    return {}

def scrap_reports_id(limit_ids):
    reports_id = []
    last_reports_id = {}

    for k, value in urls.items():
        # find pattern "/reports/xxxxxxxxxxxxxxxx"
        soup = BeautifulSoup(requests.get(value).text, "html.parser")
        for link in soup.find_all("a", href=True):
            if "/reports/" in link["href"]:
                # extract what's after "/reports/"
                report_id = link["href"][9:]

                #store first ID which will be the last id for next run
                if k not in last_reports_id:
                    last_reports_id[k] = report_id
                
                #stop if we reached limit report id
                if k in limit_ids and limit_ids[k] == report_id:
                    break
                reports_id.append(report_id)
    return {"Reports": reports_id, "LastIDs": last_reports_id}

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def send_reports_batch(reports_id):
    
    print(f"Saving in queue new reports :\n{json.dumps(reports_id)}")

    #Ids should be unique in the batch, reusing reportId directly
    formatted_messages = [{"Id": report_id, "MessageBody":report_id} for report_id in reports_id]
    for batch in list(split(formatted_messages, sqs_max_batch_size)):
        sqs.send_message_batch(QueueUrl=sqs_reports_queue, Entries=batch)

def send_last_reports(reports_id):
    print(f"Saving last ids :\n{json.dumps(reports_id)}")
    for zone, id in reports_id.items():
        dynamo.put_item(
            TableName='wclLastReportsId',
            Item={
                'zone': {
                'S': zone
                },
                'reportId': {
                'S': id
                }
            }
        )

def lambda_handler(event, ctx):
    limit_ids = get_last_reports_id()
    reports_id = scrap_reports_id(limit_ids)
    send_reports_batch(reports_id["Reports"])
    send_last_reports(reports_id["LastIDs"])
    
    return {
        'statusCode': 200
    }