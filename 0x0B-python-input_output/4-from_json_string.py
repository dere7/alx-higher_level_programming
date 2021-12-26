#!/usr/bin/python3
import json
"""
contains a function that deserializes json
"""


def from_json_string(my_str):
    """
    deserializes JSON to python obj
    :param my_str: str to be deserialized
    :return: python obj
    """
    return json.loads(my_str)
