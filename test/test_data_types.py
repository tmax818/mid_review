from data_types import *
import sys
import unittest


sys.path.insert(1, '../mid_review')


class TestMain(unittest.TestCase):

    def test_int(self):
        self.assertIsInstance(integer_type, int, "change None to an integer!")

    def test_float(self):
        self.assertIsInstance(float_type, float, "change None to a float")

    def test_str(self):
        self.assertIsInstance(str_type, str, "change None to a string!")

    def test_none(self):
        self.assertIsNone(none_type, "That one was already done!!!!")
