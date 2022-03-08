#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='dcn',
    version='0.1.0',
    description="Setup to add srf and torchdiffeq to environment",
    author="Agrim Sharma",
    author_email='agrimsharma20@gmail.com',
    url='https://github.com/agrimsharma20',
    packages=find_packages(exclude=['examples', 'info_ODE_solvers']),
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='DCN_template',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
