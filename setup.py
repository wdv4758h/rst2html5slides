#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.txt') as f:
    long_description = f.read()

setup(
    name='rst2slideshow',
    version='0.1',
    author='André Felipe Dias',
    author_email='andref.dias@gmail.com',
    setup_requires=['nose >= 1.0'],
    keywords='restructuredText slide docutils',
    description='',
    install_requires=['rst2html5'],
    zip_safe=False,
    py_modules=['rst2slideshow'],
    entry_points={
        'console_scripts': ['rst2slideshow = rst2slideshow:main', ],
    },
)