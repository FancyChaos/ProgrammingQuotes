#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Felix Scheja",
    author_email='Felix.Scheja@outlook.de',
    description="Output great/funny programming quotes. Best to use with something like fish_greeting",
    entry_points={
        'console_scripts': [
            'programmingquotes=programmingquotes.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='programmingquotes',
    name='programmingquotes',
    packages=find_packages(include=['programmingquotes']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/FancyChaos/programmingquotes',
    version='0.2.0',
    zip_safe=False,
)
