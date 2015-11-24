#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='python-upload',
    url='https://github.com/CapsLock-Studio/python-upload',
    zip_safe=True,
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'upload=upload:main'
        ]
    },
)
