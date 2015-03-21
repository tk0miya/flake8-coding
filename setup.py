# -*- coding: utf-8 -*-

from setuptools import setup
from flake8_coding import __version__


setup(
    name='flake8-coding',
    version=__version__,
    description='Adds coding magic comment checks to flake8',
    long_description=open("README.rst").read(),
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
