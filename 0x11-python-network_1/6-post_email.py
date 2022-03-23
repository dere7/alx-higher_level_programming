#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)."""
import requests
from sys import argv


if __name__ == '__main__':
    res = requests.post(argv[1], data={'email': argv[2]})
    res.encoding = 'utf-8'
    print(res.text)
