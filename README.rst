Flake8 Coding plugin
=====================

.. image:: https://travis-ci.org/tk0miya/flake8-coding.svg?branch=master
   :target: https://travis-ci.org/tk0miya/flake8-coding

.. image:: https://coveralls.io/repos/tk0miya/flake8-coding/badge.png?branch=master
   :target: https://coveralls.io/r/tk0miya/flake8-coding?branch=master

.. image:: https://codeclimate.com/github/tk0miya/flake8-coding/badges/gpa.svg
   :target: https://codeclimate.com/github/tk0miya/flake8-coding
   :alt: Code Climate


Adds coding magic comment checks (``coding:``) to ``flake8``.

Install
--------

Install with pip::

    $ pip install flake8-coding

You can check that ``flake8`` has picked it up by looking for ``flake8_coding``
in the output of ``--version``:

.. code-block:: sh

    $ flake8 --version
    2.5.4 (pep8: 1.7.0, pyflakes: 1.0.0, flake8_coding: 1.1.1, mccabe: 0.4.0) CPython 2.7.11 on Darwin

Options
-------

``accept-encodings``
~~~~~~~~~~~~~~~~~~~~

A comma-separated list of acceptable source code encodings for the ``coding:``
magic comments in files. Default is ``latin-1, utf-8``.

You can pass this as a command-line argument to ``flake8``, e.g.
``--accept-encodings=utf-8,utf-16``, or put it in your config file, e.g.:

.. code-block:: ini

    [flake8]
    accept-encodings = utf-8,utf-16

``no-accept-encodings``
~~~~~~~~~~~~~~~~~~~~~~~

If activated, this disallows all ``coding:`` magic comments, no matter their
encoding. This might be useful for Python 3 projects where UTF-8 is the default
and you don't want other encodings used in your project.

You can pass this as a command-line argument to ``flake8``, e.g.
``--no-accept-encodings``, or put it in your config file, e.g.:

.. code-block:: ini

    [flake8]
    no-accept-encodings

Rules
-----

C101 Coding magic comment not found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No magic encoding comment was found in the file. As per
`PEP-263 <https://www.python.org/dev/peps/pep-0263/>`_, this must be in the
first two lines of the file.

C102 Unknown encoding found in coding magic comment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The encoding found in the magic encoding comment did not match the
``accept-encodings`` option.

C103 Coding magic comment present
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``no-accept-encodings`` is set, and a magic encoding comment was found in the
file.

Requirements
-------------

* Python 2.6, 2.7, 3.3, 3.4
* flake8

License
--------

Apache License 2.0
