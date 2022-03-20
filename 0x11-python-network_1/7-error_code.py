#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the response."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print("Error code: {}".format(response.raise_for_status())
    print(response.text)
