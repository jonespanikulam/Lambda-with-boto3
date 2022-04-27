import boto3
client = boto3.client('ec2')
response= client.run_instances(
    ImageId='ami-03ededff12e34e59e',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
for instances in response['Instances']:
    print(instances['InstanceId'])
