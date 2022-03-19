#!/bin/bash
# Sends a request to a given URL, and displays only the status code of the response.
curl -s -w "%{http_code}" "$1"

