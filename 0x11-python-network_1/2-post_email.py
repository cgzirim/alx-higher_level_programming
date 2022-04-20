#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email as a parameter.
Displays the body of the response (decoded in utf-8)

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
