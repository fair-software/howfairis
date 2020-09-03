#!/usr/bin/env python
import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="howfairis",
    version="0.1.0",
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    license="Apache Software License 2.0",
    install_requires=[
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    extras_require={
    },
    package_data={"howfairis": ["registries.yaml"]},
)
