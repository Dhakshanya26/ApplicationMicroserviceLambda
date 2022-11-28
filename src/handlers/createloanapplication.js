// Create clients and set shared const values outside of the handler

// Create a DocumentClient that represents the query to get all items
const dynamodb = require('aws-sdk/clients/dynamodb');

const docClient = new dynamodb.DocumentClient();

// Get the DynamoDB table name from environment variables
const tableName = process.env.ApplicationTable;
const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })
const eventbridge = new AWS.EventBridge()
/**
 * A simple example includes a HTTP get method to get all items from a DynamoDB table.
 */
exports.createLoanApplicationHandler = async (event) => {
    const { httpMethod, path } = event;
    var uuid = require('uuid');
    if (httpMethod !== 'POST') {
        throw new Error(`createLoanApplication only accept Post method, you tried: ${httpMethod}`);
    }
    // All log statements are written to CloudWatch by default. For more information, see
    // https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-logging.html
    console.log('received:', JSON.stringify(event));

    // get all items from the table (only first 1MB data, you can use `LastEvaluatedKey` to get the rest of data)
    // https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#scan-property
    // https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html
     
    // Get id and name from the body of the request
    const { firstName, lastName, emailAddress, password, dateOfBirth, loanAmount } = JSON.parse(body);
    const id =uuid.v1();
    // Creates a new item, or replaces an old item with a new item
    // https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#put-property
    const paramsForDb = {
        TableName: tableName,
        Item: { id, firstName, lastName, emailAddress, password, dateOfBirth, loanAmount },
    };
    await docClient.put(params).promise();

    const response = {
        statusCode: 200,
        body,
    };

    console.log(`response from: ${path} statusCode: ${response.statusCode} body: ${response.body}`);

    console.log(`response from: ${path} statusCode: ${response.statusCode} body: ${response.body}`);
    const params = {
        Entries: [ 
          {
            Detail: JSON.stringify({
              "message": "new application added",
              "id": id
            }),
            DetailType: 'Message',
            EventBusName: 'loanApplicationEventBus',
            Source: 'createLoanApplicationHandler.event',
            Time: new Date 
          }
        ]
      }
      // Publish to EventBridge
      const result = await eventbridge.putEvents(params).promise()
      console.log(result)

    return response;
};
