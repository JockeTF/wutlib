from unittest import TestCase
from wutlib.floof import FLOOF


class TestFloof(TestCase):
    def test_floof(self):
        self.assertEqual(FLOOF, "floofy")
