#!/usr/bin/python3
"""Tests for Advent of Code 2022 day 5."""

import aoc.day5


def test_cargo9000() -> None:
    """Test first part with examples."""
    text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    text_end = """        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
"""
    ship_cargo = aoc.day5.Cargo.parse_cargo(text=text)
    assert ship_cargo.get_stack(stack=1), ["Z", "N"]
    assert ship_cargo.get_stack(stack=2), ["M", "C", "D"]
    assert ship_cargo.get_stack(stack=3), ["P"]
    for move in aoc.day5.Cargo.parse_moves(text=text):
        ship_cargo.move(move=move)
    ship_cargo_end = aoc.day5.Cargo.parse_cargo(text=text_end)
    assert ship_cargo, ship_cargo_end
    assert ship_cargo.get_top_row(), "CMZ"


def test_cargo9001() -> None:
    """Test second part with examples."""
    text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    text_end = """        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
"""
    ship_cargo = aoc.day5.Cargo9001.parse_cargo(text=text)
    assert ship_cargo.get_stack(stack=1), ["Z", "N"]
    assert ship_cargo.get_stack(stack=2), ["M", "C", "D"]
    assert ship_cargo.get_stack(stack=3), ["P"]
    for move in aoc.day5.Cargo9001.parse_moves(text=text):
        ship_cargo.move(move=move)
    ship_cargo_end = aoc.day5.Cargo9001.parse_cargo(text=text_end)
    assert ship_cargo, ship_cargo_end
    assert ship_cargo.get_top_row(), "MZD"
