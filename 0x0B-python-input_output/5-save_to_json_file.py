#!/usr/bin/python3
import json
"""
contains a function that saves serialized object to file
"""


def save_to_json_file(my_obj, filename):
    """
    saves serialized object to file
    :param my_obj: object to be serialized
    :param filename: filename to be saved to
    :return: string(JSON repr)
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
