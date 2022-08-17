import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_regions()
print(type(response))
print(response)
print("_______________________________________")
print("| "+"Endpoint" + " | " + "RegionName"+" |")
for i in response['Regions']:
    print("| "+i['Endpoint'] + " | " + i['RegionName']+" |")
print("_______________________________________")