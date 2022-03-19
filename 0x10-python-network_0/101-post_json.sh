#!/bin/bash
# Sends a JSON POST request to a given URL, and displays the body of the response.
curl -d "$(cat "$2")" -sX POST "$1"
