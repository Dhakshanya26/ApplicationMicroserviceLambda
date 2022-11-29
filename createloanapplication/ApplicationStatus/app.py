import json
import requests
import uuid
import boto3

client = boto3.client('dynamodb')
def lambda_handler(event, context): 
    input = json.loads(event['body'])
    response = client.get_item(
        TableName= 'applicationstatus',
        Key={
            'ApplicationId': {'S': input['Id']}
        }
    )
   
    print(response['Item'])
     
    response = {
        'statusCode': 200,
        'body': json.dumps({'applicationstatus':response.Item.ApplicationStatus }}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response