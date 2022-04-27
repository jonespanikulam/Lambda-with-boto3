import boto3
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
volumes = ec2.describe_volumes()
sns_arn='arn:aws:sns:us-east-1:671754373350:unusedVolume'
unused_vols= []
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 1:
        # if len(volume['Attachments']) == 0: this should be zero for unused volume. FOr testing
        # purpose have used as 1.
        unused_vols.append(volume['VolumeId'])
        #print(volume)
        print('------'*5)


email_body= "##### Unused Volumes ##### \n"
for vol in unused_vols:
    email_body= email_body + "Volume ID is {}".format(vol)



##Send email
sns.publish(
    TopicArn=sns_arn,
    Message=email_body,
    Subject='Unused Volume'
)

print(email_body)