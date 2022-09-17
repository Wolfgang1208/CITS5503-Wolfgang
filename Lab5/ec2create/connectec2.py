import boto3

def describe_ec2():
    ec2_client=boto3.client('ec2')
    instances = ec2_client.describe_instances()


    res = instances["Reservations"]
    i = 0
    for instances in res:
        x = instances['Instances'][0]['KeyName']
        if x == "22951266-key":
            i+=1
            #print(instances['Instances'][0])
            print(f"Instance{i}: ")
            print(instances['Instances'][0]['PublicIpAddress'])
            print(instances['Instances'][0]['VpcId'])
            print(instances['Instances'][0]['SubnetId'])


        
