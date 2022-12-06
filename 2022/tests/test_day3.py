#!/usr/bin/python3
"""Tests for Advent of Code 2022 day 3."""

from collections import namedtuple
from functools import reduce
from operator import and_

import aoc.day3

RucksackTest = namedtuple("RucksackTest", "text compartments common_items")


def test_rucksacks() -> None:
    """Test Rucksack class."""
    rucksacks = [
        RucksackTest("vJrwpWtwJgWrhcsFMMfFFhFp",
                     ["vJrwpWtwJgWr", "hcsFMMfFFhFp"], "p"),
        RucksackTest("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                     ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], "L"),
        RucksackTest("PmmdzqPrVvPwwTWBwg", ["PmmdzqPrV", "vPwwTWBwg"], "P"),
        RucksackTest("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", None, "v"),
        RucksackTest("ttgJtRGJQctTZtZT", None, "t"),
        RucksackTest("CrZsJsPPZsGzwwsLwLmpwMDw", None, "s"),
    ]
    total = 0
    for i in rucksacks:
        r = aoc.day3.Rucksack(contents=i.text)
        if i.compartments:
            assert r.compartments == i.compartments
        common_items = r.get_common_items()
        assert len(common_items) == 1
        e = next(iter(common_items))
        assert e, i.common_items
        total += aoc.day3.Rucksack.get_priority(item=e)
    assert total == 157


def test_item_priorities() -> None:
    priorities = [("p", 16), ("L", 38), ("P", 42), ("v", 22), ("t", 20),
                  ("s", 19)]
    for item, priority in priorities:
        assert aoc.day3.Rucksack.get_priority(item=item), priority


def test_groups() -> None:
    groups = [
        ("""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg""", "r", 18),
        ("""wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""", "Z", 52),
    ]
    total = 0
    for text, badge, priority in groups:
        rucksacks = []
        for line in iter(text.splitlines()):
            rucksacks.append(aoc.day3.Rucksack(contents=line))
        common_items = reduce(and_, map(lambda x: x.get_all_items(),
                                        rucksacks))
        assert len(common_items) == 1
        e = next(iter(common_items))
        assert e, badge
        p = aoc.day3.Rucksack.get_priority(item=e)
        assert p, priority
        total += p
    assert total == 70
