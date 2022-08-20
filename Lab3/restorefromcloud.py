import boto3
ROOT_DIR = '.'
ROOT_S3_DIR = '22951266-cloudstorage'

s3 = boto3.client("s3")

bucket_config = {'LocationConstraint': 'ap-southeast-2'}

# s3 = boto3.resource('s3')
# s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')

s3.download_file(ROOT_S3_DIR, './rootdir/rootfile.txt', './rootdir/rootfile.txt')

# print(f"{s3.list_objects(Bucket=ROOT_S3_DIR)}")

# for key in s3.list_objects(Bucket=ROOT_S3_DIR)['Contents']:
#     s3.download_file(ROOT_S3_DIR, key['Key'], key['Key'])
#     print(key['Key'])