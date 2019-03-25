import os
import json
from boto3.dynamodb.conditions import Key, Attr
import boto3

from endpoints import decimalencoder

dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch transactions from the database
    # result = table.query(
    #     Key={
    #         'id': event['pathParameters']['id']
    #     }
    # )
    uid = event['pathParameters']['uid']
    result = table.query(
        KeyConditionExpression=Key('uid').eq(uid)
    )
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
