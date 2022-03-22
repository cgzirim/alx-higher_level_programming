#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given
letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    #len(sys.argv) < 2 ? letter = "": letter = sys.argv[1]
    if len(sys.argv) < 2: letter = ""
    else: letter = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
    try:
        if len(r.json()) == 0:
            print('No result')
        else:
            d = r.json()
            print("[{}] {}".format(d.get('id'), d.get('name')))
    except ValueError:
        print("Not a valid JSON")
