import boto3
import json

client = boto3.client('kms')

response = client.create_alias(AliasName='alias/22951266_key',TargetKeyId='0ddc2bf1-7d34-4472-837b-3025fa7a4aa0')

print(response)