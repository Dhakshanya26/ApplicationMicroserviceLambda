import json
import boto3

client = boto3.client('dynamodb')
def lambda_handler(event, context): 
    print('event')
    print(event['queryStringParameters'])
    input = event['queryStringParameters']
    print(input)
    response = client.get_item(
        TableName= 'ApplicationStatus',
        Key={
            'Id': {'S': input['id']}
        }
    )
    print('response')
    print(response)
    
    if response == None:
        response = {
            'statusCode': 200,
            'body': json.dumps({'applicationstatus':'pending'),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
    else:
        response = {
            'statusCode': 200,
            'body': json.dumps({'applicationstatus':response['Item']['ApplicationStatus']['S'] }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }

    return response