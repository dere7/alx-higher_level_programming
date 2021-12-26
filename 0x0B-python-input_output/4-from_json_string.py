#!/usr/bin/python3
"""
contains a function that deserializes json
"""
import json


def from_json_string(my_str):
    """
    deserializes JSON to python obj
    :param my_str: str to be deserialized
    :return: python obj
    """
    return json.loads(my_str)
