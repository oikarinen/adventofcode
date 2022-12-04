"""Common utils for Advent of Code 2022."""
import requests
from requests.adapters import HTTPAdapter, Retry


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
