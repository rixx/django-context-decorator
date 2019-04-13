#!/usr/bin/env python

from setuptools import setup, find_packages

# Get the long description from the relevant file
try:
    with open(path.join(here, '../README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:  # noqa
    long_description = ''

setup(
    name='django_context_decorator',
    version='1.0.0',
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
    description='Conference organisation: CfPs, scheduling, much more',
    long_description=long_description,
    keywords='django context templates',
    packages=find_packages(include=['django_context_decorator']),
    url='https://github.com/rixx/django_context_decorator',
)
