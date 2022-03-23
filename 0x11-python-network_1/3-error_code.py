#!/usr/bin/python3
"""sends a request to the URL and displays the body
of the response (decoded in utf-8)"""
from urllib import request, error
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        response = request.urlopen(url)
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
    else:
        print(response.read().decode('utf-8'))
