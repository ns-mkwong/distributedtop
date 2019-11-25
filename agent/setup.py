# -*- coding: utf-8 -*-
"""Setup for the distributed top agent package.
"""
from setuptools import find_packages, setup

setup(
    name="dtop-agent",
    version="0.1.0",
    license="Proprietary",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": ["agent=agentlib.main:main"],
    }
)
