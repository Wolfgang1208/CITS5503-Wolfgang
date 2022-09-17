import boto3
import sys, getopt
options, args = getopt.getopt(sys.argv[1:], 'hp:u:', ['userid=','filename='])
# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('AWSFiles')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)

userid = ""
filename = ""

for name, value in options:
        if name in ('-f', '--filename'):
            filename = value
            print(filename)
        if name in ('-u', '--userid'):
            userid = value
            print(userid)

response = table.get_item(
    Key={
        'userId': userid,
        'filename': filename
    }
)
item = response['Item']
print(item)