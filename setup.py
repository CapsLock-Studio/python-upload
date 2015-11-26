#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-upload',
    url='https://github.com/CapsLock-Studio/python-upload',
    zip_safe=True,
    version='0.2a2',
    entry_points={
        'console_scripts': [
            'upload=upload:main'
        ]
    },
)
