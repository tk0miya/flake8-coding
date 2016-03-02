# -*- coding: utf-8 -*-

import sys
import unittest
from mock import patch
from flake8_coding import CodingChecker
from flake8.engine import get_style_guide


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
            _argv = sys.argv
            sys.argv = []
            get_style_guide(parse_argv=True)  # parse arguments
            self.assertEqual(CodingChecker.encodings, ['latin-1', 'utf-8'])
        finally:
            sys.argv = _argv
            if hasattr(CodingChecker, 'encodings'):
                del CodingChecker.encodings

    def test_change_encoding(self):
        try:
            _argv = sys.argv
            sys.argv = ['', '--accept-encodings=utf-8,utf-16']
            get_style_guide(parse_argv=True)  # parse arguments
            self.assertEqual(CodingChecker.encodings, ['utf-8', 'utf-16'])
        finally:
            sys.argv = _argv
            if hasattr(CodingChecker, 'encodings'):
                del CodingChecker.encodings

    @patch('pep8.stdin_get_value')
    def test_stdin(self, stdin_get_value):
        stdin_get_value.return_value = open('testsuite/nocodings.py').read()

        for input in ['stdin', '-', None]:
            checker = CodingChecker(None, input)
            checker.encodings = ['latin-1', 'utf-8']
            ret = list(checker.run())
            self.assertEqual(len(ret), 1)
            self.assertEqual(ret[0][0], 0)
            self.assertEqual(ret[0][1], 0)
            self.assertTrue(ret[0][2].startswith('C101 '))

    @patch.object(sys, 'argv', ['', '--no-accept-encodings'])
    def test_no_accept_encodings_sets_encodings_none(self):
        try:
            get_style_guide(parse_argv=True)  # parse arguments
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
