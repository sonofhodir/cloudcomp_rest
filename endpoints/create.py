import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        #raise Exception("Couldn't record transaction.")
        response = {
            "statusCode": 500,
            "body": "Couldn't record transaction."
        }
        return response
    try:
        text = data['text']
        timestamp = int(time.time() * 1000)
        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

        item = {
            'uid': str(uuid.uuid1()),
            'id': text['accountId'],
            'date': text['date'],
            'first_name': text['first_name'],
            'surname': text['surname'],
            'dob': text['dob'],
            'address': text['address'],
            'type': text['type'],
            'credit': text['credit'],
            'debit': text['debit'],
            'balance': text['balance'],
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }

        # write the transaction to the database
        table.put_item(Item=item)

        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(item)
        }

        return response
    except:
        # create a response
        responseFailed = {
            "statusCode": 501,
            "body": json.dumps(item)
        }

        return responseFailed
