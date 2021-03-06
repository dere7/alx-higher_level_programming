#!/usr/bin/python3
"""
contains a function that serializes object to json
"""
import json


def to_json_string(my_object):
    """
    serializes object to JSON repr
    :param my_object: object to be serialized
    :return: string(JSON repr)
    """
    return json.dumps(my_object)
