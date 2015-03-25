# -*- coding: utf-8 -*-

import re

__version__ = '1.0.1'


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

    def run(self):
        with open(self.filename) as f:
            # PEP-263 says: a magic comment must be placed into the source
            #               files either as first or second line in the file
            for lineno in range(1, 3):
                matched = re.search('coding[:=]\s*([-\w.]+)', f.readline(), re.IGNORECASE)
                if matched:
                    if matched.group(1).lower() not in self.encodings:
                        yield lineno, 0, "C102 Unknown encoding found in coding magic comment", type(self)
                    break
            else:
                yield 0, 0, "C101 Coding magic comment not found", type(self)
