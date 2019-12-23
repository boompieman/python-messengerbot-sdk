#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

__version__ = ''
with open('facebookbot/__about__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


with open('README.rst', 'r') as fd:
    long_description = fd.read()

setup(
    name="fbsdk",
    version=__version__,
    author="Sam Chang",
    author_email="t0915290092@gmail.com",
    maintainer="Sam Chang",
    maintainer_email="t0915290092@gmail.com",
    url="https://github.com/boompieman/fbsdk",
    description="Facebook Messaging API SDK for Python",
    long_description=long_description,
    license='Apache License 2.0',
    packages=[
        "facebookbot", "facebookbot.models"
    ],
    install_requires=_requirements(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ]
)
