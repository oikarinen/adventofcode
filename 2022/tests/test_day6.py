#!/usr/bin/python3
"""Tests for Advent of Code 2022 day 6."""

import aoc.day6


def test_comms() -> None:
    buffers = [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26)
        ]
    for buffer, packet_start, message_start in buffers:
        comms = aoc.day6.Comms(buffer=buffer)
        assert comms.find_first_packet_marker(length=4) == packet_start
        assert comms.find_first_packet_marker(length=14) == message_start
