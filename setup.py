#!/usr/bin/env python
import sys
from os import path
from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
django-context-decorator requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)

# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_context_decorator',
    version='1.6.0',
    author='Tobias Kunze',
    author_email='r@rixx.de',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved',
        'License :: OSI Approved :: Apache Software License',
    ],
    description='A context decorator for Django views',
    long_description=long_description,
    python_requires='>=3.6',
    keywords='django context templates',
    py_modules=['django_context_decorator'],
    url='https://github.com/rixx/django-context-decorator',
)
