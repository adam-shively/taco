from setuptools import setup, find_packages

setup(
    name='taco',
    version='0.1.1',
    packages=find_packages(include=['test2', 'test.py'])
)