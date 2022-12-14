#!/usr/bin/python3
"""Module for Advent of Code 2022 day 1."""

import heapq
from functools import reduce
from typing import Any, Dict, List

from aoc.common.utils import get_file

URL = "https://adventofcode.com/2022/day/1/input"


def process_result(text: str) -> List[Dict[str, Any]]:
    """Process string and return list of elves."""
    result = []
    items: List[int] = []
    for line in iter(text.splitlines()):
        if line == "":
            result.append({"items": items, "total": sum(items)})
            items = []
        else:
            items.append(int(line))
    return result


def main() -> None:
    """Main."""
    print("Day 1")
    result = get_file("1/input")
    elves = process_result(result)
    print("Part 1:")
    elf = reduce(lambda x, y: y if x["total"] < y["total"] else x, elves)
    print(elf["total"])
    print("Part 2:")
    top3 = sum(elf['total']
               for elf in heapq.nlargest(3, elves, key=lambda x: x["total"]))
    print(top3)


if __name__ == "__main__":
    main()
