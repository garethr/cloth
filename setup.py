#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = "cloth",
    version = "0.2",
    author = "Gareth Rushgrove",
    author_email = "gareth@morethanseven.net",
    url = "https://github.com/garethr/cloth/",

    packages = find_packages('src'),
    package_dir = {'':'src'},
    license = "MIT License",
    keywords = "fabric, ec2",
    description = "EC2 tasks and utilities for use with fabric",
    install_requires=[
        'fabric',
        'boto',
    ],
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
