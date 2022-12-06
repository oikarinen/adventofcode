#!/usr/bin/python3
"""Tests for Advent of Code 2022 day 2."""

import aoc.day2
from aoc.day2 import RPS, Round, RPSResult


def test_get_rps_score() -> None:
    rules = [
        Round(RPS.ROCK, RPS.ROCK, RPSResult.DRAW),
        Round(RPS.ROCK, RPS.PAPER, RPSResult.WIN),
        Round(RPS.ROCK, RPS.SCISSORS, RPSResult.LOST),
        Round(RPS.PAPER, RPS.ROCK, RPSResult.LOST),
        Round(RPS.PAPER, RPS.PAPER, RPSResult.DRAW),
        Round(RPS.PAPER, RPS.SCISSORS, RPSResult.WIN),
        Round(RPS.SCISSORS, RPS.ROCK, RPSResult.WIN),
        Round(RPS.SCISSORS, RPS.PAPER, RPSResult.LOST),
        Round(RPS.SCISSORS, RPS.SCISSORS, RPSResult.DRAW),
    ]
    for row in rules:
        assert aoc.day2.get_rps_score(row.opponent, row.player) == row.result


def test_parse_line() -> None:
    lines = [
        ("A Y", Round(RPS.ROCK, RPS.PAPER, RPSResult.WIN)),
        ("B X", Round(RPS.PAPER, RPS.ROCK, RPSResult.LOST)),
        ("C Z", Round(RPS.SCISSORS, RPS.SCISSORS, RPSResult.DRAW)),
    ]
    for line, r in lines:
        assert aoc.day2.parse_line(line, "part1")


def test_process_result_part1() -> None:
    text = """A Y
B X
C Z"""
    result = aoc.day2.process_result(text, "part1")
    assert sum(r["score"] for r in result) == 15
    assert [r["score"] for r in result], [8, 1, 6]


def test_process_result_part2() -> None:
    text = """A Y
B X
C Z"""
    result = aoc.day2.process_result(text, "part2")
    assert sum(r["score"] for r in result) == 12
    assert [r["score"] for r in result], [4, 1, 7]
