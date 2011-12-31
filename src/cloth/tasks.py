#! /usr/bin/env python

from collections import defaultdict

from fabric.api import run, env, sudo, task, runs_once, roles

from cloth.utils import instances, use


env.nodes = []
env.roledefs = defaultdict(list)


@task
def all():
    "All nodes"
    for node in instances():
        use(node)

@task
def preview():
    "Preview nodes"
    for node in instances('^preview-'):
        use(node)

@task
def production():
    "Production nodes"
    for node in instances('^production-'):
        use(node)

@task
def nodes(exp):
    "Select nodes based on a regular expression"
    for node in instances(exp):
        use(node)

@task
@runs_once
def list():
    "List EC2 name and public and private ip address"
    for node in env.nodes:
        print "%s (%s, %s)" % (node.tags["Name"], node.ip_address,
            node.private_ip_address)

@task
def uptime():
    "Show uptime and load"
    run('uptime')

@task
def free():
    "Show memory stats"
    run('free')

@task
def updates():
    "Show package counts needing updates"
    run("cat /var/lib/update-notifier/updates-available")

@task
def upgrade():
    "Upgrade packages with apt-get"
    sudo("apt-get update; apt-get upgrade -y")

