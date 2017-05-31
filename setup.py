#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

install_requires = ['flask-cors', 'guessit', 'flask-restful>=0.3.6']
if sys.version_info < (2, 7):
    install_requires.extend(['argparse'])

setup_requires = ['pytest-runner']

dev_require = ['zest.releaser[recommended]', 'pylint', 'tox', 'pylint']

tests_require = ['pytest', 'pytest-flask', 'pytest-mock']
if sys.version_info < (3, 3):
    tests_require.extend(['mock'])

entry_points = {
    'console_scripts': [
        'guessit-rest = guessitrest.__main__:main'
    ],
}

with io.open('guessitrest/__version__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]$', f.read(), re.MULTILINE).group(1)

args = dict(name='guessit-rest',
            version=version,
            description='GuessIt - REST WebService',
            long_description=README,
            # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
            classifiers=['Development Status :: 5 - Production/Stable',
                         'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                         'Operating System :: OS Independent',
                         'Intended Audience :: Developers',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.3',
                         'Programming Language :: Python :: 3.4',
                         'Topic :: Multimedia',
                         'Topic :: Software Development :: Libraries :: Python Modules'
                         ],
            keywords='python library release parser name filename movies series episodes animes',
            author='Rémi Alvergnat',
            author_email='toilal.dev@gmail.com',
            url='http://github.com/guessit-io/guessit-rest',
            license='LGPLv3',
            packages=find_packages(),
            include_package_data=True,
            install_requires=install_requires,
            setup_requires=setup_requires,
            tests_require=tests_require,
            entry_points=entry_points,
            test_suite='guessitrest.test',
            zip_safe=True,
            extras_require={
                'test': tests_require,
                'dev': dev_require
            })

setup(**args)
