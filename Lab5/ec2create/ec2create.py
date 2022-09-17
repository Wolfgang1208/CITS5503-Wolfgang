import boto3

ec2 = boto3.resource('ec2')

aws_region = 'ap-southeast-2'

az_1 = 'ap-southeast-2a'
az_2 = 'ap-southeast-2b'

ami_id = 'ami-d38a4ab1'

keyname = '22951266-key'

Groupid = '22951266-sg'

def createInstances(az):
    instance = ec2.create_instances(
    ImageId = ami_id,
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = keyname,
    SecurityGroupIds = [Groupid],
    Placement = {'AvailabilityZone':az})
    return instance

instance1 = createInstances(az_1)
instance2 = createInstances(az_2)
