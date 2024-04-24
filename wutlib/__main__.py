from sys import argv
from wutlib.cli import cli
from wutlib.floof import FLOOF

assert FLOOF == "floofy"


def main() -> None:
    exit(cli(*argv))


main()
