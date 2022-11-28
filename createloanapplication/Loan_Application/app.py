import json
import requests
import uuid
import boto3

client = boto3.client('dynamodb')
def lambda_handler(event, context):
    print(event)
    input = json.loads(event['body'])
    data = client.put_item(
        TableName = 'applications',
        Item = {
            'id': {
                'S':  str(uuid.uuid1())
            },
            'firstname': {
                'S': input['firstname']
            },
            'lastname': {
                'S': input['lastname']
            }
        }
    )

    data2 = client.scan(
        TableName = 'applications'
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