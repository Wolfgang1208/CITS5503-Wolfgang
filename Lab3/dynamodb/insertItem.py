import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('AWSCloudFiles')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)

table.put_item(
   Item={
        'userId': '22951266-cloudstorage',
        'owner': 'mdanwarulkaium.patwary',
        'filename': 'rootfile.txt',
        'path': './rootdir',
        'lastUpdated': '2022-08-18 04:57:28+00:00',
        'permission': 'FULL_CONTROL'
    }
)

response = table.get_item(
    Key={
        'userId': '22951266-cloudstorage',
        'owner': 'mdanwarulkaium.patwary'
    }
)
item = response['Item']
print(item)