#!/usr/bin/python3
""" Web server
"""
from crypt import methods
import json
from random import random
from flask import Flask, request, make_response
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Root
    """
    res = make_response('Hello, I\'m Index')
    res.headers['X-Request-Id'] = random() * 100
    return res


@app.route('/post_email', methods=["GET", "POST"])
def post_email():
    return f'Your email is: {request.form["email"]}'


@app.route('/search_user', methods=['POST'])
def search_user():
    users = [
        {'id': 2, 'name': 'User1'},
        {'id': 4, 'name': 'User2'},
    ]
    q = request.query_string.decode('utf-8').split('=')[1]
    print(q)
    if not q:
        return 'tet'
    for u in users:
        if q in u['name']:
            return json.dumps(u)
    return ''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
