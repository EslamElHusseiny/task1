import os
import yaml
import json
import sys
import boto3

print("Creating new stack ... ")
f = open(os.environ["Template"],'r')
template = f.read()
f.close()

client = boto3.client('cloudformation')
client.create_stack(
    StackName=os.environ["StackName"],
    TemplateBody= template,
    Parameters=os.environ["Parameters"],
    TimeoutInMinutes=123,
)
