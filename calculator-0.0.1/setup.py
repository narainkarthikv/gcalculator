#!/usr/bin/python
from setuptools import setup
__author__ = "Narainkarthik"
setup(
 name="calculator",
 version="0.0.1",
 description="A simple calculator to calculate basic mathematical operations",
 author="Narainkarthik",
 author_email="narainkarthik812@gmail.com",
 license="GNU",
 url="https://github.com/narainkarthikv/gcalculator",
 packages=["tvb"],
 entry_points={
 "console_scripts": [
 "tvb=tvb:main",
 ]
 },
)
