# -*- coding: utf-8 -*-

import re
import pep8

__version__ = '1.1.1'


class CodingChecker(object):
    name = 'flake8_coding'
    version = __version__

    def __init__(self, tree, filename):
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--accept-encodings', default='latin-1, utf-8', action='store',
            help="Acceptable source code encodings for `coding:` magic comment"
        )
        parser.config_options.append('accept-encodings')

    @classmethod
    def parse_options(cls, options):
        cls.encodings = [e.strip().lower() for e in options.accept_encodings.split(',')]

    def read_headers(self):
        if self.filename in ('stdin', '-', None):
            return pep8.stdin_get_value().splitlines(True)[:2]
        else:
            return pep8.readlines(self.filename)[:2]

    def run(self):
        try:
                # PEP-263 says: a magic comment must be placed into the source
                #               files either as first or second line in the file
                lines = self.read_headers()
                if len(lines) == 0:
                    raise StopIteration()

                for lineno, line in enumerate(lines, start=1):
                    matched = re.search('coding[:=]\s*([-\w.]+)', line, re.IGNORECASE)
                    if matched:
                        if matched.group(1).lower() not in self.encodings:
                            yield lineno, 0, "C102 Unknown encoding found in coding magic comment", type(self)
                        break
                else:
                    yield 0, 0, "C101 Coding magic comment not found", type(self)
        except IOError:
            pass
