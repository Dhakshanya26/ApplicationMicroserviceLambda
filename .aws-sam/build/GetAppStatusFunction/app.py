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
            'Id': {'S': input['Id']}
        }
    ) 
    try: 
        if response['Item'] is None:
            output = {
                'statusCode': 200,
                'body': json.dumps({'applicationstatus':'pending'}),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
            }
        else:
            output = {
                'statusCode': 200,
                'body': json.dumps({'applicationstatus':response['Item']['ApplicationStatus']['S'] }),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
            }
        
    except:
        output = {
            'statusCode': 200,
            'body': json.dumps({'applicationstatus':'pending'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
    return output