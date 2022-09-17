import boto3
import os 
import numpy as np

ROOT_DIR = '.'
ROOT_S3_DIR = '22951266-cloudstorage'

s3 = boto3.client("s3")

bucket_config = {'LocationConstraint': 'ap-southeast-2'}

g = os.walk("./")  

dirArray=[]

key_id = "383f1927-fbbe-4471-8b8d-3503e44b88aa"

for path,dir_list,file_list in g:  
    for dir_name in dir_list:
        print(type(os.path.join(path, dir_name)))
        print(os.path.join(path, dir_name))
        dirArray.insert(-1,os.path.join(path, dir_name))

# debug only
# print(dirArray)

for key in s3.list_objects(Bucket=ROOT_S3_DIR)['Contents']:
    currKey = key['Key'].split(sep='/', maxsplit=-1)[0:-1]
    currKey='./'+'/'.join(currKey)

    if not os.path.exists(currKey):
        print(f"Not exists! {currKey}")
        os.makedirs(currKey)
    else:
        print(f"Exists! {currKey}")     
    s3.download_file(ROOT_S3_DIR, key['Key'], key['Key'])

    # debug only
    # print(currKey)
    # print(key['Key'])

print("Done")