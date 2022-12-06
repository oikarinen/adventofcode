#!/usr/bin/python3
"""Module for Advent of Code 2022 day 4."""

import re
from functools import reduce
from typing import List, NamedTuple, Set

import aoc
from aoc.common.utils import get_file

SectionRange = NamedTuple("SectionRange", [("low", int), ("high", int)])


class Assignment():
    """Section assignment for a pair of elves."""

    def __init__(self, *, ranges: List[SectionRange]) -> None:
        """Initialize Section Assignment object."""
        self.ranges: List[Set[int]] = list(
            map(lambda x: set(range(x.low, x.high + 1)), ranges))

    def is_fully_contained(self) -> bool:
        """Return True if one of the ranges of the assignment is fully contained in the others."""
        i = reduce(lambda a, b: a.intersection(b), self.ranges)
        for r in self.ranges:
            if r == i:
                return True
        return False

    def is_overlap(self) -> bool:
        """Return True if ranges overlap at all."""
        return bool(reduce(lambda a, b: a.intersection(b), self.ranges))


def process_result(text: str) -> List[Assignment]:
    """Process the list of section assignments."""
    line_re = re.compile(
        r"^(?P<low1>\d+)-(?P<high1>\d+),(?P<low2>\d+)-(?P<high2>\d+)")
    result = []
    for line in iter(text.splitlines()):
        m = line_re.match(line)
        if not m:
            raise Exception(f"Invalid input: {line}")
        assignment = aoc.day4.Assignment(ranges=[
            SectionRange(int(m.group("low1")), int(m.group("high1"))),
            SectionRange(int(m.group("low2")), int(m.group("high2")))
        ])
        result.append(assignment)
    return result


def main() -> None:
    """Main."""
    print("Day 4")
    print("Part 1")
    result = get_file("4/input")
    total1 = len([a for a in process_result(result) if a.is_fully_contained()])
    print(total1)
    print("Part 2")
    total2 = len([a for a in process_result(result) if a.is_overlap()])
    print(total2)


if __name__ == "__main__":
    main()
