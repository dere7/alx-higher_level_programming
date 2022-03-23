#!/usr/bin/python3
"""sends a request to the URL and displays the body
of the response (decoded in utf-8)"""
import requests
from sys import argv


if __name__ == '__main__':
    try:
        res = requests.get(argv[1])
        res.raise_for_status()
    except requests.HTTPError as e:
        print(f'Error code: {e.response.status_code}')
    else:
        res.encoding = 'utf-8'
        print(res.text)
