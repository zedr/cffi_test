#!/usr/bin/env python

from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='cffi-test',
    version='1.0',
    description='CFFI test',
    author='zedr',
    author_email='zedr@zedr.com',
    url='http://example.org',
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=['cffi', 'Cython'],
    setup_requires=['cffi', 'Cython'],
    cffi_modules=[
        'src/c_ext/build.py:ffi'
    ],
    ext_modules = cythonize("src/cython_test/vectors.py")
)
