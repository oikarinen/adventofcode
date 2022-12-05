#!/usr/bin/python3
"""Tests for Advent of Code 2022 day 2."""

from functools import reduce
from operator import and_

import aoc.day4
from aoc.day4 import Assignment, SectionRange


def test_assignment() -> None:
    """Test Assignment class."""

    assignment1 = Assignment(ranges=[SectionRange(2, 4), SectionRange(6, 8)])
    assert assignment1.ranges, [{2, 3, 4}, {6, 7, 8}]
    assignment2 = Assignment(ranges=[SectionRange(2, 3), SectionRange(4, 5)])
    for r in assignment2.ranges:
        assert len(r), 2
    assignment3 = Assignment(ranges=[SectionRange(5, 7), SectionRange(7, 9)])
    for r in assignment3.ranges:
        assert len(r), 3


def test_assingments() -> None:
    """Test example assignments for being fully containing in each other."""
    assignments = [
        ("2-4,6-8", False, False),
        ("2-3,4-5", False, False),
        ("5-7,7-9", False, True),
        ("2-8,3-7", True, True),
        ("6-6,4-6", True, True),
        ("2-6,4-8", False, True),
    ]
    total_contains = 0
    total_overlaps = 0
    for text, contains, overlaps in assignments:
        for a in aoc.day4.process_result(text):
            if a.is_fully_contained():
                assert contains
                total_contains += 1
            if a.is_overlap():
                assert overlaps
                total_overlaps += 1

    assert total_contains == 2
    assert total_overlaps == 4
