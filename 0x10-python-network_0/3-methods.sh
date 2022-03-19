#!/bin/bash
#Displays all HTTP methods the server will accept.
curl -sX "OPTIONS" "$1"
