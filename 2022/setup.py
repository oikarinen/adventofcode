#!/usr/bin/env python
"""Setup module for Advent of Code 2022."""


from setuptools import setup

setup(
    name="aoc",
    version="0.1",
    description="Advent of Code 2022",
    author="Tapio",
    url="https://github.com/oikarinen/adventofcode",
    packages=["aoc"],
    entry_points={
        "console_scripts": [
            "main = aoc.main:main",
        ],
    },
    install_requires=[
        "flake8",
        "isort",
        "pep8",
        "pylint",
        "yapf",
        "requests",
    ],
)
