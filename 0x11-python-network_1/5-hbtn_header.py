#!/usr/bin/python3
"""Sends a request to a given URL and displays the value of the variable
X-Request-Id in the response header.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
