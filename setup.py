#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()


extras_require = {
    'mailgun': [
        'django-mailgun==0.8.0',
    ],
    'raven': [
        'raven==5.8.1',
    ],
}


requires = [
    'Django==2.0.1',
    'dj-database-url==0.3.0',
    'django-braces==1.8.1',
    'django-configurations==1.0',
    'django-crispy-forms==1.7.1',
    'django-grappelli==2.10.1',
    'django-model-utils==2.4',
    'envdir==0.7',
    'psycopg2-binary==2.7.4',
    'pytz==2015.7',
    'rules==1.3.0',
]


setup(
    name='dsa_merchant',
    version='0.1.0',
    description='A trading and shopping aid for the "Das Schwarze Auge" RPG.',
    long_description=read(BASE_DIR, 'README.rst'),
    author='ninjaduck.solutions',
    author_email='contact@ninjaduck.solutions',
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],
    install_requires=requires,
    license='AGPL3',
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',

        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
