"""Common utils for Advent of Code 2022."""


def get_file(file_name):
    """Read file from disk."""
    with open(file_name, encoding="utf8") as f:
        return f.read()
