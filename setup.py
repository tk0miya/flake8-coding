# -*- coding: utf-8 -*-
import re

from setuptools import setup


def get_version(filename):
    """
    Return package version as listed in `__version__` in `filename`.
    """
    init_py = open(filename).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('flake8_coding.py')


with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='flake8-coding',
    version=version,
    description='Adds coding magic comment checks to flake8',
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
    ],
    author='Takeshi KOMIYA',
    author_email='i.tkomiya at gmail.com',
    url='https://github.com/tk0miya/flake8-coding',
    license='Apache License 2.0',
    keywords='pep8 flake8 coding',
    py_modules=['flake8_coding'],
    install_requires=[
        'flake8',
    ],
    entry_points={
        'flake8.extension': ['C10 = flake8_coding:CodingChecker'],
    },
)
