import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('jones123456789')
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)