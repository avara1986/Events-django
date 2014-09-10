# -*- coding: utf-8 -*-
# Copyright (c) 2014 by Alberto Vara <a.vara.1986@gmail.com>


import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="Django Events",
    version="0.0.1",
    author="Alberto Vara",
    author_email="a.vara.1986@gmail.com",
    description="Django Events App",
    long_description=(read('README.rst') + '\n\n' + read('CHANGES.rst')),
    classifiers=[
        'Development Status :: 1 - Beta',
        'Framework :: Django Rest Framework',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="LGPL 3",
    keywords="django, CMS, events",
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='setuptest.setuptest.SetupTestSuite',
)