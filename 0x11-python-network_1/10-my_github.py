#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, auth=(argv[1], argv[2]), headers=headers)
    user = res.json()
    try:
        print(user['id'])
    except KeyError:
        print(None)
