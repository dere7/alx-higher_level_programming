#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)."""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
