#!/usr/bin/env python
"""Setup module for Advent of Code 2022."""


from setuptools import find_packages, setup  # type: ignore

with open("requirements.txt", "r", encoding="utf8") as f:
    requirements = f.read().splitlines()

setup(
    name="aoc",
    version="0.1",
    description="Advent of Code 2022",
    author="Tapio",
    url="https://github.com/oikarinen/adventofcode",
    packages=find_packages(exclude=["tests"]),
    package_data={"aoc": ["py.typed"]},
    entry_points={
        "console_scripts": [
            "main = aoc.main:main",
        ],
    },
    install_requires=requirements,
)
