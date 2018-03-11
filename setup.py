# -*- coding: utf-8 -*-

from os import path
from codecs import open
from setuptools import setup, find_packages


setup(
    name='slash-commads',
    version='1.0.0',
    description='Framework for writing slack slash commands easily',
    long_description='visit https://github.com/akhilputhiry/slash-commands for more details',
    url='https://github.com/akhilputhiry/slash-commands',
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
    keywords='slack',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
        'celery==4.1.0',
        'requests==2.18.4',
    ],
)
