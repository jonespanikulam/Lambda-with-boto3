import boto3
s3 = boto3.client('s3')
file_reader= open('s3BucketCreate.py').read()
response = s3.put_object(
    ACL='private',
    Body= file_reader,
    Bucket='jones123456789',
    Key='demo')
