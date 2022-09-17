import boto3
import json

client = boto3.client('kms')

response = client.create_key(
    Description='22951266kmskey',
    KeyUsage='ENCRYPT_DECRYPT',
    Origin='AWS_KMS',
    MultiRegion=False
)

print(response)