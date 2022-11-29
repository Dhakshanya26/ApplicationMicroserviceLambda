import json
import requests
import uuid
import boto3

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

    data2 = client.scan(
        TableName = 'applications'
    )

    eventClient = boto3.client('events')
    detailJsonString = '{"Id":"applicationId"}'

    publishedEventResponse = eventClient.put_events(
        Entries=[
            {
                'Source':'user-event',
                'DetailType':'user-preferences',
                'Detail':detailJsonString,
                'EventBusName':'LoanApplicationEventBus' 
            }
        ]
    )
    response = {
        'statusCode': 200,
        'body': json.dumps(data2),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response