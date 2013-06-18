#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup

with open('README.txt') as f:
    long_description = f.read()

setup(
    name='rst2html5slides',
    version='0.2',
    author='André Felipe Dias',
    author_email='andref.dias@gmail.com',
    keywords='restructuredText slide docutils',
    description='',
    install_requires=['rst2html5'],
    zip_safe=False,
    py_modules=['rst2html5slides'],
    entry_points={
        'console_scripts': ['rst2html5slides = rst2html5slides:main', ],
    },
)
