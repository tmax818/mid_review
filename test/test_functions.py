from functions import *
import sys
import unittest

from unittest.mock import patch

sys.path.insert(1, '../mid_review')


class TestFunctions(unittest.TestCase):

    message = '\033[31m' + 'Change code in functions.py!''\033[39m'

    @patch('builtins.print')
    def test_hello(self, mock_print):
        hello()
        mock_print.assert_called_with('Hello, World!')

    @patch('builtins.print')
    def test_hello_name(self, mock_print):
        hello_name('John')
        mock_print.assert_called_with('Hello, John')

    def test_is_even(self):
        self.assertEqual(is_even(4), True, self.message)
        self.assertFalse(is_even(5), self.message)

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), 'fizz', self.message)
        self.assertEqual(fizz_buzz(5), 'buzz', self.message)
        self.assertEqual(fizz_buzz(15), 'fizzbuzz', self.message)
