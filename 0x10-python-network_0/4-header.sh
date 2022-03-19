#!/bin/bash
# Sends a GET request to a given URL, and displays the body of the response.
curl -d '{"X-School-User-Id":"98"}' -sX GET "$1"
