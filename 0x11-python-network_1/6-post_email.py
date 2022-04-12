#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email as a parameter.
Displays the body of the response.

Usage: 6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
