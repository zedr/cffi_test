#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='cff_test',
    version='1.0',
    description='CFFI test',
    author='zedr',
    author_email='zedr@zedr.com',
    url='http://example.org',
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=['cffi'],
    setup_requires=['cffi'],
    cffi_modules=[
        'cffi/build.py:ffi'
    ]
)
