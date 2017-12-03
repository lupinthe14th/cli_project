#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

from setuptools import setup, find_packages

import cli_app

install_requires = [
    'schematics>=2.0.1'
]

def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()


setup(
    name='cli',
    version=cli_app.__version__,
    description=cli_app.__doc__.strip(),
    long_description=long_description(),
    url='http://www.ordinarius-fectum.net/',
    download_url='https://github.com/lupinthe14th/cli_app',
    author=cli_app.__author__,
    author_email='hideosuzuki@ordinarius-fectum.net',
    license=cli_app.__licence__,
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'cli = cli_app.__main__:main',
        ],
    },
    install_requires=install_requires,
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

# vim fileencoding=utf-8
