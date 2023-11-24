#! /usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='django-tabbed-admin',
    use_scm_version=True,
    author='Guillaume Pousseo',
    author_email='guillaumepousseo@revsquare.com',
    description='Easily add tabs to django admin forms.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
