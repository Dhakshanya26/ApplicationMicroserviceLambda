import json  
 
def lambda_handler(event, context): 
     
    response = {
        'statusCode': 200,
        'body': json.dumps({"totalscore":event['CalculatedScore']['CreditScore'] + event['CalculatedScore']['FraudScore']}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response