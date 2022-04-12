#!/bin/bash
#Sends request to a given URL. Displays the size of the body of the response.
curl -s "$1" | wc -c
