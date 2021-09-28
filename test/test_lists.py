from lists import *
import sys
import unittest

from unittest.mock import patch

sys.path.insert(1, '../mid_review')


class TestLogic(unittest.TestCase):

    def test_california(self):
        self.assertEqual(california, "California")

    def test_last_two(self):
        self.assertEqual(last_two_states, ["Oregon", "California"])
