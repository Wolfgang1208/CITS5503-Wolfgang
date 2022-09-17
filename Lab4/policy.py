import json
import boto3

# Create a bucket policy
bucket_name = '22951266-cloudstorage'
bucket_policy = {
  "Version": "2012-10-17",
  "Statement": {
   "Sid": "AllowAllS3ActionsInUserFolderForUserOnly",
    "Effect": "DENY",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::22951266-cloudstorage/rootdir/*",
    "Condition": {
      "StringNotLike": {
          "aws:username":"22951266@student.uwa.edu.au"
       }
    }
  }
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
response = s3.get_bucket_policy(Bucket=bucket_name)
print(response)