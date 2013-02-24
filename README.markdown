A set of tasks for use with Fabric and EC2.

## Installation

Now available on PyPi at http://pypi.python.org/pypi/cloth. Installation is therefore as simple as:

    pip install cloth

## Configuration

Export your EC2 credntials as environment variables.

    export AWS_EC2_REGION=eu-west-1
    export AWS_ACCESS_KEY_ID=<your-access-key>
    export AWS_SECRET_ACCESS_KEY=<your-secret-key>

## Usages

To use just import some or all of the tasks into your fabric file. Or
create a blank fabfile.py with the following contents.

    #! /usr/bin/env python
    from cloth.tasks import *

This will give you a good few commands.

    ⚡ fab -l
    Available commands:

      all         All nodes
      free        Show memory stats
      list        List EC2 name and public and private ip address
      nodes       Select nodes based on a regular expression
      preview     Preview nodes
      production  Production nodes
      updates     Show package counts needing updates
      upgrade     Upgrade packages with apt-get
      uptime      Show uptime and load

Of most interest should be the 'all' and 'nodes' tasks. These allow you
to load EC2 instances for further command running.

    ⚡ fab all list

The above should list all of your EC2 instances including the name and
public and private ip addresses.

    ⚡ fab nodes:"^production.*" list

The above should list all of your EC2 instances that start with
'production'. This takes a regex as the argument so you can get whatever
instances you like.


    ⚡ fab all uptime

As an example of running a command on a set of EC2 instances try the
above. This should show the uptime and load averages for all your EC2
instances. Use -P as well to have that happen in parallel.


## Opinionated Tasks

I generally use a convention for the names of my EC2 machines, in
particular:

    <platform>-<role>-<unique-identifier>

The production and preview tasks simple filter for those with a platform
value of production or preview. More interesting is that roles are being
set based on the second part of the name. For instance if I have a set
of instances called:

* production-backend-1
* production-backend-2
* production-backend-3
* production-proxy
* production-database

I could write a task like so:

    @task
    @roles('backend')
    def passenger():
        "Show details about passenger performance"
        sudo('passenger-memory-stats')
        sudo('passenger-status')

The run that task with:

    ⚡ fab all passenger

That task would only be run on the three backend instances.

