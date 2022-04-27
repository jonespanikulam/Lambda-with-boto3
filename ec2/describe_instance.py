import boto3
client= boto3.client('ec2')
reponse= client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ]
)

for instances in reponse['Reservations']:
    for instanceid in instances['Instances']:
        print("the instance id of running instance is {}".format(instanceid['InstanceId']))