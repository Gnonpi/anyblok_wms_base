# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok / WMS Base project
#
#    Copyright (C) 2018 Georges Racinet <gracinet@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from setuptools import setup, find_packages
import os

version = '0.0.1'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'r',
          encoding='utf-8') as readme_file:
    README = readme_file.read()

with open(
    os.path.join(here, 'doc', 'CHANGES.rst'), 'r', encoding='utf-8'
) as change:
    CHANGES = change.read()

anyblok_init = [
]

requirements = [
    'anyblok',
    'anyblok_postgres',
    'psycopg2'
]

setup(
    name='anyblok_wms_base',
    version=version,
    description="Warehouse Management and Logistics, base Anyblok modules",
    long_description=README + '\n' + CHANGES,
    author="Georges Racinet",
    author_email='gracinet@anybox.fr',
    url="http://docs.anyblok-wms-base.anyblok.org/%s" % version,
    packages=find_packages(),
    entry_points={
        'bloks': [
            'wms-core=anyblok_wms_base.bloks.wms_core:WmsCore',
        ],
        'test_bloks': [
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='stock logistics wms',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=requirements + ['nose'],
)
