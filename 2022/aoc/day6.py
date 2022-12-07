#!/usr/bin/python3
"""Module for Advent of Code 2022 day 6."""

import aoc
from aoc.common.utils import get_file


class Comms():
    """Parse elven protocol."""
    PACKET_START_LENGTH = 4

    def __init__(self, *, buffer: str) -> None:
        self.buffer = buffer

    def find_first_packet_marker(self, *, length: int = PACKET_START_LENGTH) -> int:
        """Return end position of first packet marker."""
        for i in range(0, len(self.buffer)):
            if self.is_packet_marker(position=i, length=length):
                return i+length
        raise Exception("packet marker not found")

    def is_packet_marker(self, *, position: int = 0, length: int) -> bool:
        """Return True if none of the characters is repeated in the input."""
        return len(set(self.buffer[position:position+length])) == length


def main() -> None:
    """Main."""
    print("Day 6")
    print("Part 1")
    result = get_file("6/input")
    comms = aoc.day6.Comms(buffer=result)
    print(comms.find_first_packet_marker(length=4))
    print("Part 2")
    print(comms.find_first_packet_marker(length=14))


if __name__ == "__main__":
    main()
