import re
import os
import json
import boto3
import datetime
import uuid
from datetime import datetime
import json
 
 
 
class Secrets:
    def __init__(self):
        self.AWS_ACCESS_KEY = "xx"
        self.AWS_SECRET_KEY = "xx"
        self.AWS_REGION_NAME = "us-east-1"
        self.EventBusName = 'xxxxxx'
 
class AWSEventBus(Secrets):
 
    """Helper class to which add functionality on top of boto3 """
 
    def __init__(self, **kwargs):
        Secrets.__init__(
            self
        )
        self.client = boto3.client(
            "events",
            aws_access_key_id=self.AWS_ACCESS_KEY,
            aws_secret_access_key=self.AWS_SECRET_KEY,
            region_name=self.AWS_REGION_NAME,
        )
 
    def send_events(self, json_message={}):
        response = self.client.put_events(
            Entries=[
                {
                    'Time': datetime.now(),
                    'Source': 'Producer',
                    'Resources': [],
                    'DetailType': 'string',
                    'Detail':json.dumps(json_message) ,
                    'EventBusName': self.EventBusName,
 
 
                },
            ]
        )
        return response
 
def main():
    """"
    {
	"detail":{
    	"status":["new order"]
    }
    }
    """
    json_data = {
        "status":"new order",
        "message":"Vijay has bought new iphone 13"
    }
    helper = AWSEventBus()
    message = helper.send_events(json_message=json_data)
    print(message)
 
main()