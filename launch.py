import os
import yaml
import json
import sys
import boto3
import glob

TemplateFile = glob.glob('./*.template')
YamlFile = glob.glob('./*.yaml')

with open(YamlFile[0], 'r') as r:
    Parm = yaml.load(r)

f = open(TemplateFile[0],'r')
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


