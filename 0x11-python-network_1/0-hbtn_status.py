#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        is_utf = 'OK' if response.headers.get_content_charset() else 'NO'
        print(f'Body response:\n\t- type: {type(data)}')
        print(f'\t- content: {data}\n\t- utf8 content: {is_utf}')
