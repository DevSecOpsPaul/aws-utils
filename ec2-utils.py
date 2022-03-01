#!/usr/bin/env python

"""ec2 inventory script
"""

from __future__ import print_function
import os
import sys
from urllib import response
import boto3

ec2_resource = boto3.resource('ec2')

def instance_info_function():
    instance_info = ec2_resource.instances.filter(
        InstanceIds=[
            i["InstanceId"],
        ],
    )

def list_instances_function():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running',
                ]
            },
        ],
        MaxResults=1000,
    )
    print(response)

list_instances_function()