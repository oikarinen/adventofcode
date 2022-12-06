#!/usr/bin/python3
"""Module for Advent of Code 2022 day 2."""

from collections import namedtuple
from enum import Enum
from typing import Any, Dict, List

from aoc.common.utils import get_file


class RPS(Enum):
    """Rock, Paper, Scissors option."""
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RPSResult(Enum):
    """Rock, Paper, Scissors result."""
    LOST = 0
    DRAW = 3
    WIN = 6


Round = namedtuple("Round", "opponent player result")


def get_rps_score(opponent: RPS, player: RPS) -> RPSResult:
    """Calculate RPS score for a round."""
    if player.value == opponent.value:
        return RPSResult.DRAW
    if player.value == (opponent.value + 1):
        return RPSResult.WIN
    if player == RPS.ROCK and opponent == RPS.SCISSORS:
        return RPSResult.WIN
    return RPSResult.LOST


def _parse_opponent_move(line: str) -> RPS:
    """A for Rock, B for Paper, and C for Scissors."""
    if line[0] == "A":
        return RPS.ROCK
    if line[0] == "B":
        return RPS.PAPER
    if line[0] == "C":
        return RPS.SCISSORS
    raise Exception(f"Unknown opponent selection: {line}")


def _parse_player_move(line: str) -> RPS:
    """X for Rock, Y for Paper, and Z for Scissors."""
    if line[2] == "X":
        return RPS.ROCK
    if line[2] == "Y":
        return RPS.PAPER
    if line[2] == "Z":
        return RPS.SCISSORS
    raise Exception(f"Unknown player selection: {line}")


def _parse_result_move(opponent: RPS, line: str) -> RPS:
    """X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win."""
    if line[2] == "X":
        return [
            option for option in RPS
            if get_rps_score(opponent, option) == RPSResult.LOST
        ][0]
    if line[2] == "Y":
        return [
            option for option in RPS
            if get_rps_score(opponent, option) == RPSResult.DRAW
        ][0]
    if line[2] == "Z":
        return [
            option for option in RPS
            if get_rps_score(opponent, option) == RPSResult.WIN
        ][0]
    raise Exception(f"Unknown player selection: {line}")


def parse_line(line: str, strategy: str) -> Round:
    """Parse strategy for a single line."""
    opponent = _parse_opponent_move(line)
    if strategy == "part1":
        player = _parse_player_move(line)
        return Round(opponent, player, get_rps_score(opponent, player))
    # default is part2
    player = _parse_result_move(opponent, line)
    return Round(opponent, player, get_rps_score(opponent, player))


def process_result(text: str, strategy: str) -> List[Dict[str, Any]]:
    """Process strategy guide as string and return list of elves."""
    result = []
    for line in iter(text.splitlines()):
        r = parse_line(line, strategy)
        result.append({"score": r.player.value + r.result.value, "round": r})
    return result


def main() -> None:
    """Main."""
    print("Day 2")
    strategy = get_file("2/input")
    print("Part 1")
    rounds = process_result(strategy, "part1")
    score = sum(r["score"] for r in rounds)
    print(score)
    print("Part 2")
    rounds = process_result(strategy, "part2")
    score = sum(r["score"] for r in rounds)
    print(score)


if __name__ == "__main__":
    main()
