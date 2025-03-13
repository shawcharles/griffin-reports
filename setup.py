# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------

#


# -----------------------------------------------------------------------------
"""Setup script for griffin_reports."""

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def get_version(module='griffin_reports'):
    """Get version."""
    with open(os.path.join(HERE, module, '_version.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.rst'), 'r') as f:
        data = f.read()
    return data


REQUIREMENTS = ['griffin', 'pweave', 'matplotlib']


setup(
    name='griffin-reports',
    version=get_version(),
    keywords=['Griffin', 'Plugin'],
    url='https://github.com/shawcharlesgriffin-reports',
    license='MIT',
    author='Griffin Project Contributors',
    author_email='info@griffin-analytics.com',
    description='Griffin plugin for Markdown reports using Pweave.',
    long_description=get_description(),
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    package_data={'griffin_reports.utils': ['*.md']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ])
