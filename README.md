# Lambda-with-boto3

1) stopped-ec2-instances
  
  Here the module 'requests' is imported and packaged in 'Layers'.
  Slack webhook can be passed directly or encrypted using the KMS keys.
  Cloudwatch event is given as triggger and rule is set to the alert for stopped instance to lambda function
  
  .![1](https://user-images.githubusercontent.com/59678465/165510750-5968a55c-4b70-4ce6-b336-438109df875e.jpg)
  
  
  2) unused-volumes

  Find all unused volumes and sent email using sns

![image](https://user-images.githubusercontent.com/59678465/165514596-95f6cc7e-0117-4419-9a61-d45206a9efeb.png)

3) dynamodb-json-s3

When a json file uploaded to s3, the lambda function automatically process the file and put the data in dynamodb
