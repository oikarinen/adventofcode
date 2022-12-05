#!/usr/bin/python3
"""Module for Advent of Code 2022 day 3."""

from functools import reduce
from operator import add, and_
from typing import List, Set

import aoc
from aoc.common.utils import get_file

GROUP_SIZE = 3  # number of elves in a group


class Rucksack():
    """Rucksack."""

    def __init__(self, *, contents: str) -> None:
        """Initialize rucksack object."""
        if len(contents) % 2:
            raise Exception(f"Not even length string: {contents}")
        m = int(len(contents) / 2)
        self.compartments: List[str] = [contents[0:m], contents[m:]]  # pylint: disable=unsubscriptable-object

    def get_common_items(self) -> Set[str]:
        """Return all comon items in the rucksack compartments."""
        return set(self.compartments[0]) & set(self.compartments[1])

    def get_all_items(self) -> Set[str]:
        """Return all items in the rucksack."""
        return set("".join(self.compartments))

    @classmethod
    def get_priority(cls, *, item: str) -> int:
        """Return priority for the item."""
        if not item or len(item) > 1:
            raise Exception(f"Invalid input: {item}")
        if item.isupper():
            return 27 + ord(item) - ord("A")
        return 1 + ord(item) - ord("a")


def process_result(text: str) -> List[Rucksack]:
    """Process ist of rucksacks."""
    result = []
    for line in iter(text.splitlines()):
        rucksack = aoc.day3.Rucksack(contents=line)
        common_items = rucksack.get_common_items()
        if len(common_items) != 1:
            raise Exception(
                f"Invalid input: more than 1 common items ({common_items}) for rucksack (line: {line})"
            )
        result.append(rucksack)
    return result


def main() -> None:
    """Main."""
    print("Day 3")
    print("Part 1")
    rucksacks = get_file("3/input")
    result = process_result(rucksacks)
    total1 = reduce(
        add,
        map(lambda x: aoc.day3.Rucksack.get_priority(item=x),
            map(lambda e: next(iter(e.get_common_items())), result)))
    print(total1)
    print("Part 2")
    total2 = 0
    for group_rucksacks in [
            result[i:i + GROUP_SIZE] for i in range(0, len(result), GROUP_SIZE)
    ]:
        common_items = reduce(
            and_, map(lambda x: x.get_all_items(), group_rucksacks))
        if len(common_items) != 1:
            raise Exception(
                f"Invalid input: more than 1 common items ({common_items}) for group"
            )
        total2 += aoc.day3.Rucksack.get_priority(item=next(iter(common_items)))
    print(total2)


if __name__ == "__main__":
    main()
