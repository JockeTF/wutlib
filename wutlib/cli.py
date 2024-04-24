from wutlib.floof import FLOOF


def cli(*args: str) -> str | None:
    if len(args) > 1:
        return "This isn't an argument clinic!"

    print(f"Floof is {FLOOF}!")

    return None
