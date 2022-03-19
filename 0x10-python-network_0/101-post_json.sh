#!/bin/bash
# Sends a JSON POST request to a given URL, and displays the body of the response.
curl -d "@$2" -X POST "$1"
