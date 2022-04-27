import boto3
client= boto3.resource('ec2')
for instances in client.instances.filter(
    Filters=[{
            'Name': 'instance-state-name',
            'Values': [
                'running'
    ]}]
):
    print("instance id is {} and instance type is {} ".format(instances.instance_id,instances.instance_type))