import boto3

session = boto3.Session(
    region_name=REGIONS,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=TOKEN_KEY
    )

client = session.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
for i in regions:
    cnt=0
    ec2 = boto3.resource('ec2', i)
    instances = ec2.instances.filter()
    # # If I want to filter with running ec2's
    # instances = ec2.instances.filter(
    # Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        cnt+=1
    print(i,"\t", cnt)





##! This script get ec2's on all regions
# * Author: Shadi Badir