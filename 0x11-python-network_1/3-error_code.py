#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the response."""
import sys
import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print("Error code: {}".format(e.reason))
