from tokenize import ContStr
from urllib import response
import boto3
import json
import re

ROOT_S3_DIR = '22951266-cloudstorage'

s3 = boto3.client("s3")

response = s3.get_bucket_acl(Bucket=ROOT_S3_DIR)

permission = response['Grants'][0]['Permission']

response = s3.list_objects(Bucket=ROOT_S3_DIR)

# debug only
# print(response)

contents = response['Contents']

i = 1

for items in contents:

    # debug only
    # print("--------------------------------")
    # print("UserId:")
    # print(response['Name'])
    # print()
    # print("FileName:")
    # print(items['Key'].split('/')[-1])
    # print()
    # print("Path:")
    # print(f"{items['Key'].split('/')[0:-1]}")
    # print()
    # print("LastModified time:")
    # print(items['LastModified'])
    # print()
    # print("Owner:")
    # print(items['Owner']['DisplayName'])

    # ver 1
    # text = {}
    # text["TableName"] = "CloudFile"
    # text["userId"] = '{"S":'+response['Name']+'}'
    # text["filename"] = '{"S":'+items['Key'].split('/')[-1]+'}'
    # text["path"] = '{"S":'+'./'+'/'.join(items['Key'].split('/')[0:-1])+'}'
    # text["lastUpdated"] = '{"S":'+str(items['LastModified'])+'}'
    # text["owner"] = '{"S":'+items['Owner']['DisplayName']+'}'
    # text["permission"] = '{"S":'+permission+'}'

    # ver 2
    # text = {}
    # text["TableName"] = "CloudFile"
    # text.setdefault('userId',{})['S'] = response['Name']
    # text.setdefault('filename',{})['S'] = items['Key'].split('/')[-1]
    # text.setdefault('path',{})['S'] = './'+'/'.join(items['Key'].split('/')[0:-1])
    # text.setdefault('lastUpdated',{})['S'] = str(items['LastModified'])
    # text.setdefault('owner',{})['S'] = items['Owner']['DisplayName']
    # text.setdefault('permission',{})['S'] = permission

    text = {}
    # text["TableName"] = "CloudFile"
    text["userId"] = response['Name']
    text["filename"] = items['Key'].split('/')[-1]
    text["path"] = './'+'/'.join(items['Key'].split('/')[0:-1])
    text["lastUpdated"] = str(items['LastModified'])
    text["owner"] = items['Owner']['DisplayName']
    text["permission"] = permission

    # debug only
    # print(text)

    jsondata = json.dumps(text,  indent=4, separators=(",", ": "),default=str)
    # jsondata = re.escape(jsondata)
    f = open('dynamodb/'+'info'+str(i)+'File.json','w')
    f.write(jsondata)
    f.close()
    i=i+1

# response = s3.get_bucket_acl(Bucket=ROOT_S3_DIR)
# print("--------------------------------")
# print("Permission:")
# print(response['Grants'][0]['Permission'])