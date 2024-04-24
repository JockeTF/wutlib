from unittest import TestCase
from wutlib.cli import cli


class TestMain(TestCase):
    def test_main(self):
        self.assertIsNone(cli("wutlib"))

    def test_help(self):
        self.assertEqual(
            cli("wutlib", "--help"),
            "This isn't an argument clinic!",
        )
