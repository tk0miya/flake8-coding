# -*- coding: utf-8 -*-

import unittest
from flake8_coding import CodingChecker


class TestFlake8Coding(unittest.TestCase):
    def test_has_utf8_coding_header(self):
        checker = CodingChecker(None, 'testsuite/utf8.py')
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


if __name__ == '__main__':
    unittest.main()
