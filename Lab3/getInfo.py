from tokenize import ContStr
from urllib import response
import boto3
import json

ROOT_S3_DIR = '22951266-cloudstorage'

s3 = boto3.client("s3")

response = s3.list_objects(Bucket=ROOT_S3_DIR)

print(response)

contents = response['Contents']

for items in contents:
    print("--------------------------------")
    print("UserId:")
    print(response['Name'])
    print()
    print("FileName:")
    print(items['Key'].split('/')[-1])
    print()
    print("Path:")
    print(f"{items['Key'].split('/')[0:-1]}")
    print()
    print("LastModified time:")
    print(items['LastModified'])
    print()
    print("Owner:")
    print(items['Owner']['DisplayName'])
    text = {}
    text["TableName"] = "CloudFile"
    text["userId"] = response['Name']
    text["filename"] = items['Key'].split('/')[-1]
    text["path"] = './'+'/'.join(items['Key'].split('/')[0:-1])
    text["lastUpdated"] = items['LastModified']
    text["owner"] = items['Owner']['DisplayName']

response = s3.get_bucket_acl(Bucket=ROOT_S3_DIR)
print("--------------------------------")
print("Permission:")
print(response['Grants'][0]['Permission'])

print(text)