import boto3
source_region= 'us-east-1'
ec2 = boto3.resource('ec2',region_name= source_region)
instances= ec2.instances.filter(InstanceIds=['i-08b1760867ecad203'])
image_ids=[]
for instance in instances:
    image = instance.create_image(Name='demo boto' + instance.id, Description='demo-boto' + instance.id)
    image_ids.append(image.id)

print("image to be copied {}".format(image_ids))

#### wait foe image to be availble

client = boto3.client('ec2',region_name= source_region)
waiter = client.get_waiter('image_available')

waiter.wait( Filters=[{
            'Name': 'image-id',
            'Values': image_ids
        }])
###### copy image to region eu-est-1 ireland
destination_region= 'eu-west-1'
client = boto3.client('ec2',region_name= destination_region)
for image_id in image_ids:
    client.copy_image(Name='boto3 image' + image_id , SourceImageId =image_id, SourceRegion='us-east-1')