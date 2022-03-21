#!/bin/bash
# sends a POST request and displays the response body
curl -sd 'email=test@gmail.com&subject="I will always be here for PLD' "$1"
