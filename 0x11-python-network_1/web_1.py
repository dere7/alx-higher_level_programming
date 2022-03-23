#!/usr/bin/python3
""" Web server
"""
from crypt import methods
import json
from random import random
from flask import Flask, jsonify, request, make_response
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


@app.route("/search_user", methods=['POST'], strict_slashes=False)
def search_user():
    data = {}
    q = request.form.get("q")
    print(request.url, q)
    if q is not None and type(q) is str and len(q) > 0 and ord(q[0]) in range(97,123):
        first_letter = q[0]
        data['name'] = "{}{}".format(q, "olberton")
        data['id'] = 89
    res = jsonify(data)
    res.headers["Content-Type"] = "application/json"
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
