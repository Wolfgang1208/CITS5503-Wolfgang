import os
from urllib import response
import boto3
import base64
# import sys, getopt
# ------------------------------
# CITS5503
#
# cloudstorage.py
#
# skeleton application to copy local files to S3
#
# Given a root local directory, will return files in each level and
# copy to same path on S3
#
# ------------------------------ 


ROOT_DIR = '.'
ROOT_S3_DIR = '22951266-cloudstorage'

s3 = boto3.client("s3")

bucket_config = {'LocationConstraint': 'ap-southeast-2'}

# options, args = getopt.getopt(sys.argv[1:], 'hp:i:', ['initialise='])
    

    
def upload_file(folder_name, file, file_name):
    print(f"{file} {ROOT_S3_DIR} {file_name}")
    # ./rootdir/rootfile.txt rootfile.txt
    # response = s3.upload_file(file,ROOT_S3_DIR,file_name)
    # print(response)
    s3.upload_file(file,ROOT_S3_DIR,file)
    print("Uploading %s" % file)

# Main program
# Insert code to create bucket if not there

try:
    # ver 0.1
    # for name, value in options:
    #     if name in ('-i', '--initialise'):
    #         print(type(value))
    #         if value == "True":
    #             print("Yes from initialise.")
    #             response = s3.create_bucket(Bucket=ROOT_S3_DIR,CreateBucketConfiguration=bucket_config)
    #             # response = s3.list_buckets()
    #             print(response)

    
    print(response)
except Exception as error:
    pass

# parse directory and upload files

for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
    if dir_name != ROOT_DIR:
        for fname in file_list:
            upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)

print("done")

