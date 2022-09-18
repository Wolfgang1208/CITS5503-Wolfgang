import boto3

def describe_ec2():
    ec2_client=boto3.client('ec2')
    instances = ec2_client.describe_instances()


    res = instances["Reservations"]
    #print(res)
    i = 1
    for instances in res:
        x = instances['Instances'][0]['KeyName']
        if x == "22951266-key":
            if 'PublicIpAddress' in instances['Instances'][0]:
                #print(instances['Instances'][0])
                print("---------------------")
                print(f"Instance{i}: ")
                print(instances['Instances'][0]['PublicIpAddress'])
                print(instances['Instances'][0]['VpcId'])
                print(instances['Instances'][0]['SubnetId'])
                i+=1


describe_ec2()
