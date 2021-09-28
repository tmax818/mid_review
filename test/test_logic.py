from logic import *
import sys
import unittest

from unittest.mock import patch

sys.path.insert(1, '../mid_review')


class TestLogic(unittest.TestCase):

    def test_is_greater(self):
        self.assertTrue(is_greater(10, 5))
