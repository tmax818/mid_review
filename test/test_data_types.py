from data_types import *
import sys
import unittest


sys.path.insert(1, '../mid_review')


class TestMain(unittest.TestCase):

    message = '\033[31m' + 'Change code in data_types.py!''\033[39m'

    def test_int(self):
        self.assertIsInstance(integer_type, int, self.message)

    def test_float(self):
        print(self.longMessage)
        self.assertIsInstance(float_type, float, self.message)

    def test_str(self):
        self.assertIsInstance(str_type, str, self.message)

    def test_none(self):
        self.assertIsNone(none_type, self.message)
