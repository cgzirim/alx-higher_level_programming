#!/usr/bin/python3
"""Sends a request to a given URL and displays the value of the X-Request-Id 
variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
       print(response.getheader('X-Request-Id'))
