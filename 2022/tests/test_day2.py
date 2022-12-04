#!/usr/bin/python3
"""Tests for Advent of Code 2022 day 2."""

import aoc.day2
from aoc.day2 import RockPaperScissors, Round, RPSResult


def test_get_rps_score():
    rules = [
        Round(RockPaperScissors.ROCK, RockPaperScissors.ROCK, RPSResult.DRAW),
        Round(RockPaperScissors.ROCK, RockPaperScissors.PAPER, RPSResult.WIN),
        Round(RockPaperScissors.ROCK, RockPaperScissors.SCISSORS,
              RPSResult.LOST),
        Round(RockPaperScissors.PAPER, RockPaperScissors.ROCK, RPSResult.LOST),
        Round(RockPaperScissors.PAPER, RockPaperScissors.PAPER,
              RPSResult.DRAW),
        Round(RockPaperScissors.PAPER, RockPaperScissors.SCISSORS,
              RPSResult.WIN),
        Round(RockPaperScissors.SCISSORS, RockPaperScissors.ROCK,
              RPSResult.WIN),
        Round(RockPaperScissors.SCISSORS, RockPaperScissors.PAPER,
              RPSResult.LOST),
        Round(RockPaperScissors.SCISSORS, RockPaperScissors.SCISSORS,
              RPSResult.DRAW),
    ]
    for row in rules:
        assert aoc.day2.get_rps_score(row.opponent, row.player) == row.result


def test_parse_line():
    lines = [
        ("A Y",
         Round(RockPaperScissors.ROCK, RockPaperScissors.PAPER,
               RPSResult.WIN)),
        ("B X",
         Round(RockPaperScissors.PAPER, RockPaperScissors.ROCK,
               RPSResult.LOST)),
        ("C Z",
         Round(RockPaperScissors.SCISSORS, RockPaperScissors.SCISSORS,
               RPSResult.DRAW)),
    ]
    for line, r in lines:
        assert aoc.day2.parse_line(line, "part1")


def test_process_result_part1():
    text = """A Y
B X
C Z"""
    result = aoc.day2.process_result(text, "part1")
    assert sum(r["score"] for r in result) == 15
    assert [r["score"] for r in result] == [8, 1, 6]


def test_process_result_part2():
    text = """A Y
B X
C Z"""
    result = aoc.day2.process_result(text, "part2")
    assert sum(r["score"] for r in result) == 12
    assert [r["score"] for r in result] == [4, 1, 7]
