#!/bin/bash
# sends delete request and displays the body of the response
curl -s -i "$1" | grep "Allow" | cut -c 8-
