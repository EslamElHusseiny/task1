import os
import yaml
import json
import sys
import boto3

os.system("git clone " + os.environ["Repo"] + " app")

with open(os.environ["Parameters"], 'r') as r:
    Parm = yaml.load(r)

f = open(os.environ["Template"],'r')
template = f.read()
f.close()

var=[]
for key, value in Parm.iteritems():
   temp = { 'ParameterKey': key , 'ParameterValue': value }
   var.append(temp)


client = boto3.client('cloudformation')
client.create_stack(
    StackName = os.environ["StackName"],
    TemplateBody = template,
    Parameters = var,
    TimeoutInMinutes = 123,
)


