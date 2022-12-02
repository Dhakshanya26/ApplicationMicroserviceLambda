import json  
 
def lambda_handler(event, context): 
     
    response = {
        'statusCode': 200,
        'body': json.dumps({"creditscore": 1}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response