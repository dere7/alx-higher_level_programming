#!/usr/bin/python3
"""takes in a letter and sends a POST request to
with the letter as a parameter."""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': argv[1] if len(argv) >= 2 else ''}
    try:
        res = requests.post(url, params=params)
        if res.text == '':
            print('No result')
        else:
            user = res.json()
            print(f'[{user["id"]}] {user["name"]}')
    except requests.exceptions.JSONDecodeError as e:
        print('Invalid JSON')
 