from unittest import TestCase
from services.task import find_by

class TestFail(TestCase):

    def test__find_by__completed_and_title_none(self):
        with self.assertRaises(ValueError):
            find_by()
