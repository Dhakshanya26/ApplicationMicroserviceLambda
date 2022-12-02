import json  
 
def lambda_handler(event, context): 
     
    response = {
        'statusCode': 200,
        'body': json.dumps({
            "id": event['Id'],
            "loanAmount": int(event['ApplicationDetail']['Item']['loanAmount']['S']),
            "totalscore":event['CalculatedScore']['CreditScore'] + event['CalculatedScore']['FraudScore'] 
        }),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response