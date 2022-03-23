#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {'per_page': 10}
    res = requests.get(url, params=params, headers=headers)
    commits = res.json()
    try:
        for commit in commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except KeyError:
        print(None)
