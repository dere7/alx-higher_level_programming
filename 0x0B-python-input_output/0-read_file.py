#!/usr/bin/python3
"""
contains a function that reads a text file
"""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout
    :param filename: file name to read from
    :return: None
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
