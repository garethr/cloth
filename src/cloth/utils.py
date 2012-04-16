#! /usr/bin/env python

import re
import os

import boto.ec2
from fabric.api import env


REGION = os.environ.get("AWS_EC2_REGION")

def ec2_instances():
    "Use the EC2 API to get a list of all machines"
    region = boto.ec2.get_region(REGION)
    reservations = region.connect().get_all_instances()
    instances = []
    for reservation in reservations:
        instances += reservation.instances
    return instances

def instances(exp=".*"):
    "Filter list of machines matching an expression"
    expression = re.compile(exp)
    instances = []
    for node in ec2_instances():
        if node.tags and node.ip_address:
            try:
                if expression.match(node.tags.get("Name")):
                    instances.append(node)
            except TypeError:
                pass
    return instances

def use(node):
    "Set the fabric environment for the specifed node"
    try:
        role = node.tags.get("Name").split('-')[1]
        env.roledefs[role] += [node.ip_address]
    except IndexError:
        pass
    env.nodes += [node]
    env.hosts += [node.ip_address]

