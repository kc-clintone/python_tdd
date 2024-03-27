from distutils.core import setup
from setuptools import find_packages


setup(
    name="python_tdd",
    version="0.0.1",
    description="A simple fullstack app with flask",
    packages=find_packages(include=['static','templates'])
)
