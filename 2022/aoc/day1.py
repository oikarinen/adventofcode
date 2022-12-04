#!/usr/bin/python3
"""Module for Advent of Code 2022 day 1."""

import heapq
from functools import reduce

import requests
from requests.adapters import HTTPAdapter, Retry

URL = "https://adventofcode.com/2022/day/1/input"


def get_file_url(url, headers):
    """Read file from URL."""
    session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    session.mount("http://", HTTPAdapter(max_retries=retries))
    result = session.get(url, headers=headers)
    if result.status_code != 200:
        raise Exception(f"Failed to fetch {url}: {result.status_code}")
    return result.text


def get_file(file_name):
    """Read file from disk."""
    with open(file_name, encoding="utf8") as f:
        return f.read()


def process_result(text):
    """Process string and return list of elves."""
    result = []
    items = []
    for line in iter(text.splitlines()):
        if line == "":
            result.append({"items": items, "total": sum(items)})
            items = []
        else:
            items.append(int(line))
    return result


def main():
    """Main."""
    # headers = {"cookie": "session=XXX"}
    # result = get_file(URL, headers)
    result = get_file("1/input")
    elves = process_result(result)
    print("Part 1:")
    elf = reduce(lambda x, y: y if x["total"] < y["total"] else x, elves)
    print(elf["total"])
    print("Part 2:")
    top3 = sum(elf['total']
               for elf in heapq.nlargest(3, elves, key=lambda x: x['total']))
    print(top3)


if __name__ == "__main__":
    main()
