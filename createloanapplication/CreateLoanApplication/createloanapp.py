import json
import requests
import uuid
import boto3 
from boto3.dynamodb.conditions import Key, Attr
client = boto3.client('dynamodb')
def lambda_handler(event, context): 
    input = json.loads(event['body'])
    applicationId = str(uuid.uuid1())
    data = client.put_item(
        TableName = 'applications',
        Item = {
            'Id': {
                'S':  applicationId
            },
            'firstname': {
                'S': input['firstname']
            },
            'lastname': {
                'S': input['lastname']
            },
            'emailAddress': {
                'S': input['emailAddress']
            },
            'loanAmount': {
                'S': input['loanAmount']
            } 
        }
    )
    eventClient = boto3.client('events')
    detailJsonString = {"Id":applicationId}

    publishedEventResponse = eventClient.put_events(
        Entries=[
            {
                'Source':'com.aws.submitloanapp',
                'DetailType':'Order Notification',
                'Detail':json.dumps(detailJsonString),
                'EventBusName':'LoanAppEventBus' 
            }
        ]
    )
    response = {
        'statusCode': 200,
        'body': json.dumps(detailJsonString),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response