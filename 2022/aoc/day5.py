#!/usr/bin/python3
"""Module for Advent of Code 2022 day 5."""

from __future__ import annotations

import re
from typing import Dict, List, NamedTuple, Type

import aoc
from aoc.common.utils import get_file

CargoMove = NamedTuple("CargoMove", [("source", int), ("destination", int),
                                     ("count", int)])


class Cargo():
    """Elves' ship cargo, with CrateMover 9000."""

    stack_re = re.compile(r"\[(?P<crate>[A-Z])\]")
    move_re = re.compile(
        r"^move (?P<count>\d+) from (?P<source>\d+) to (?P<destination>\d+)$")

    def __init__(self, *, stacks: Dict[int, List[str]]) -> None:
        """Initialize Cargo object."""
        self.stacks: Dict[int, List[str]] = stacks

    def get_stack(self, *, stack: int) -> List[str]:
        """Return stack in a position."""
        result = self.stacks.get(stack)
        if not result:
            raise Exception(f"Stack not found: {stack}")
        return result

    def move(self, *, move: CargoMove) -> None:
        """Move crates between stacks."""
        if self.stacks.get(move.source, None) is None or self.stacks.get(
                move.destination, None) is None:
            raise Exception(
                f"Stack not found: {move.source} or {move.destination}")
        if move.count < 0:
            raise NotImplementedError("Moving negative counts not implemented")
        for _i in range(move.count):
            crate = self.stacks[move.source].pop()
            self.stacks[move.destination].append(crate)

    def get_top_row(self) -> str:
        """Return a string concatenating crates on top of the stacks."""
        # TODO: the stack ids need to be ordered :(
        result = []
        for _k, v in sorted(self.stacks.items()):
            result.append(v[-1])
        return "".join(result)

    @classmethod
    def parse_cargo(cls, *, text: str) -> Cargo:
        """Return a new Cargo object with the stacks read from input."""
        stacks: Dict[int, List[str]] = {}
        for line in iter(text.splitlines()):
            if line == "":
                break
            # match cargo row
            n = len("[X] ")
            for i in range(0, len(line), n):
                m = cls.stack_re.match(line[i:i + n])
                if not m:
                    continue
                j = int(1 + i / n)  # stack index
                stack = stacks.get(j, None)
                if stack is None:
                    stacks[j] = []
                stacks[j].insert(0, m.group("crate"))
        return cls(stacks=stacks)

    @classmethod
    def parse_moves(cls, *, text: str) -> List[CargoMove]:
        """Return list of moves from parsed text. Note: skips until first empty line."""
        result = []
        skip = True
        for line in iter(text.splitlines()):
            # skip from beginning until empty line
            if line == "":
                skip = False
                continue
            if skip:
                continue
            m = cls.move_re.match(line)
            if not m:
                raise Exception(f"Invalid input: {line}")
            result.append(
                CargoMove(int(m.group("source")), int(m.group("destination")),
                          int(m.group("count"))))
        return result


class Cargo9001(Cargo):
    """Elves' ship cargo, with CrateMover 9001."""

    def move(self, *, move: CargoMove) -> None:
        """Move crates between stacks."""
        if self.stacks.get(move.source, None) is None or self.stacks.get(
                move.destination, None) is None:
            raise Exception(
                f"Stack not found: {move.source} or {move.destination}")
        if move.count < 0:
            raise NotImplementedError("Moving negative counts not implemented")
        crates: List[str] = []
        for _i in range(move.count):
            crates.insert(0, self.stacks[move.source].pop())
        self.stacks[move.destination] += crates


def process_result(text: str, cls: Type[Cargo]) -> Cargo:
    """Process the input text including setting up new Cargo and the moves."""
    cargo = cls.parse_cargo(text=text)
    for move in cls.parse_moves(text=text):
        cargo.move(move=move)
    return cargo


def main() -> None:
    """Main."""
    print("Day 5")
    print("Part 1")
    result = get_file("5/input")
    cargo1 = process_result(result, aoc.day5.Cargo)
    print(cargo1.get_top_row())
    print("Part 2")
    cargo2 = process_result(result, aoc.day5.Cargo9001)
    print(cargo2.get_top_row())


if __name__ == "__main__":
    main()
