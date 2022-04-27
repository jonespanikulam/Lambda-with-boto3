import boto3
s3 = boto3.client('s3')
response = s3.list_objects(
    Bucket='jones123456789')
for objects in response['Contents']:
    print(objects['Key'])

