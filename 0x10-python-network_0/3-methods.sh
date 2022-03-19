#!/bin/bash
#Displays all HTTP methods the server of a given URL will accept.
curl -sX OPTIONS "$1"
