import json
import requests

slack_webhook='https://hooks.slack.com/services/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'

def send_slack(event, context):
    print(str(event))
    slack_message= {'text': 'Ec2 instance Stopped'}
    resp= requests.post(slack_webhook,data=json.dumps(slack_message))
    return resp.text