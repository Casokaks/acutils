"""
acutils setup
==================================
Casokaks's python utility library.

Author: Casokaks (https://github.com/Casokaks/)
Created on: Aug 15th 2021

"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

from setuptools import setup, find_packages
setup(
    name='acutils',
    version='0.2.2',
    author='Casokaks',
    author_email='casokaks@gmail.com',
    description='Collection on python utility functions.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Casokaks/acutils',
    project_urls = {
        "Bug Tracker": "https://github.com/Casokaks/acutils/issues"
    },
    license='NO PERMISSION TO USE, DISTRIBUTE, REPRODUCE, REPLICATE OR CREATE DERIVATIVE WORKS WITHOUT AUTHOR CONSENT.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'matplotlib',
        'plotly',
    ],
)
