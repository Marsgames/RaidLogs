import json
import boto3
import os

lambda_client = boto3.client("lambda")
lambda_function_name = os.environ["LAMBDA_TO_REVIVE"]


def set_lambda_concurrency():
    lambda_client.put_function_concurrency(
        FunctionName=lambda_function_name,
        ReservedConcurrentExecutions=int(os.environ["CONCURRENCY_LIMIT"]),
    )


def lambda_handler(event, context):
    set_lambda_concurrency()
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
