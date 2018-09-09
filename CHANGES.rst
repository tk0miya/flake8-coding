Changelog
=========

1.3.1 (2016-09-09)
------------------
* Fix bugs

  - #14 Can't read from stdin using flake8-coding and flake8-print at the same time
  - #16 flake8-coding fails on python 3.7 with "RuntimeError: generator raised StopIteration"

1.3.0 (2016-08-20)
------------------
* Drop Python 2.6 support
* Fix a bug

  - Fix no-accept-encodings to work in config files

1.2.2 (2016-06-28)
------------------
* Fix a bug

  - Could not work under flake8 >= 3.0

1.2.1 (2016-05-20)
------------------
* Add option `no-accept-encodings`. If set, will warn for files containing a `coding:` magic comment.
* Fix a bug

  - #4 stdin not supported

1.2.0 (not released)
--------------------

1.1.1 (2015-10-25)
------------------
* Fix a bug

  - Fix #2 ignore errors if target file is not found

1.1.0 (2015-06-27)
------------------
* Do not warn for empty file (Thanks to gforcada)

1.0.1 (2015-03-25)
------------------
* Fix a bug

  - Fix typo in option name: accept-encodings

1.0.0 (2015-03-21)
------------------
* Initial release
