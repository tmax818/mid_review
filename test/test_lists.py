from lists import *
import sys
import unittest

from unittest.mock import patch

sys.path.insert(1, '../mid_review')


class TestLists(unittest.TestCase):

    message = '\033[31m' + 'Change code in lists.py!''\033[39m'

    def test_california(self):
        self.assertEqual(california, "California", self.message)

    def test_last_two(self):
        self.assertEqual(last_two_states, [
                         "Oregon", "California"], self.message)

    def test_has_item(self):
        self.assertTrue(has_item(my_list, "alpha"), self.message)
