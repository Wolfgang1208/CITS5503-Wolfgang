import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='AWSFiles',
    KeySchema=[
        {
            'AttributeName': 'userId',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'filename',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'userId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'filename',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 6,
        'WriteCapacityUnits': 6
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)