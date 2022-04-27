import boto3
client= boto3.client('ec2')
response= client.stop_instances(
    InstanceIds=['i-036c646a05a1e2104'])
print('instance stopped')
