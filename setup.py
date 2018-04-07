# coding=utf-8

from os import path
from codecs import open
from setuptools import setup, find_packages


setup(
    name='slashcommands',
    version='1.0.0',
    description='Framework for writing slash commands',
    long_description='visit https://github.com/puthiry-lab/slash-commands for more details',
    url='https://github.com/puthiry-lab/slash-commands',
    author='Akhil Lawrence',
    author_email='akhilputhiry@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'celery==4.1.0',
        'redis==2.10.6',
        'flask==0.12.2',
        'psutil==5.4.3',
        'requests==0.18.4',
    ],
)
