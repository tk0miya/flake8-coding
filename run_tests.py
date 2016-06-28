# -*- coding: utf-8 -*-

import unittest
from mock import patch
from collections import namedtuple
from flake8_coding import CodingChecker


Options = namedtuple('Options', 'no_accept_encodings, accept_encodings')


class TestFlake8Coding(unittest.TestCase):
    def test_has_utf8_coding_header(self):
        checker = CodingChecker(None, 'testsuite/utf8.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_file_not_found(self):
        checker = CodingChecker(None, 'file_not_found')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_empty_file(self):
        checker = CodingChecker(None, 'testsuite/empty.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_has_latin1_coding_header(self):
        checker = CodingChecker(None, 'testsuite/latin1.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_has_coding_header_at_2nd_line(self):
        checker = CodingChecker(None, 'testsuite/2nd-line.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_has_coding_header_at_3rd_line(self):
        checker = CodingChecker(None, 'testsuite/3rd-line.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 0)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('C101 '))

    def test_has_vim_styled_coding_header(self):
        checker = CodingChecker(None, 'testsuite/vim-style.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_has_coding_header_with_invalid_encoding_name(self):
        checker = CodingChecker(None, 'testsuite/invalid.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('C102 '))

    def test_has_no_coding_headers(self):
        checker = CodingChecker(None, 'testsuite/nocodings.py')
        checker.encodings = ['latin-1', 'utf-8']
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 0)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('C101 '))

    def test_default_encoding(self):
        try:
            options = Options(False, 'latin-1, utf-8')
            CodingChecker.parse_options(options)
            self.assertEqual(CodingChecker.encodings, ['latin-1', 'utf-8'])
        finally:
            if hasattr(CodingChecker, 'encodings'):
                del CodingChecker.encodings

    def test_change_encoding(self):
        try:
            options = Options(False, 'utf-8,utf-16')
            CodingChecker.parse_options(options)
            self.assertEqual(CodingChecker.encodings, ['utf-8', 'utf-16'])
        finally:
            if hasattr(CodingChecker, 'encodings'):
                del CodingChecker.encodings

    def test_stdin(self):
        try:
            import pycodestyle as pep8  # noqa
            target = 'pycodestyle.stdin_get_value'
        except ImportError:
            import pep8  # noqa
            target = 'pep8.stdin_get_value'

        with patch(target) as stdin_get_value:
            with open('testsuite/nocodings.py') as fp:
                stdin_get_value.return_value = fp.read()

            for input in ['stdin', '-', None]:
                checker = CodingChecker(None, input)
                checker.encodings = ['latin-1', 'utf-8']
                ret = list(checker.run())
                self.assertEqual(len(ret), 1)
                self.assertEqual(ret[0][0], 0)
                self.assertEqual(ret[0][1], 0)
                self.assertTrue(ret[0][2].startswith('C101 '))

    def test_no_accept_encodings_sets_encodings_none(self):
        try:
            options = Options(True, 'latin-1,utf-8')
            CodingChecker.parse_options(options)
            self.assertTrue(CodingChecker.encodings is None)
        finally:
            if hasattr(CodingChecker, 'encodings'):
                del CodingChecker.encodings

    def test_encoding_none_with_no_coding_comment(self):
        checker = CodingChecker(None, 'testsuite/nocoding.py')
        checker.encodings = None
        ret = list(checker.run())
        self.assertEqual(ret, [])

    def test_encoding_none_with_coding_comment(self):
        checker = CodingChecker(None, 'testsuite/utf8.py')
        checker.encodings = None
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 0)
        self.assertTrue(ret[0][2].startswith('C103 '))

if __name__ == '__main__':
    unittest.main()
