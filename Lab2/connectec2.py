import boto3
ec2_client=boto3.client('ec2')
instances = ec2_client.describe_instances()

instanceip = "BFG"
res = instances["Reservations"]
for instances in res:
    x = instances['Instances'][0]['KeyName']
    if x == "22951266-key":
        instanceip = instances['Instances'][0]['PublicIpAddress']

print(instanceip)
        
