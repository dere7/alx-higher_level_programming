#!/usr/bin/python3
"""
contains a function that load deserialized object from file
"""
import json


def load_from_json_file(filename):
    """
    loads deserialized object from file
    :param filename: filename to be saved to
    :return: object
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
