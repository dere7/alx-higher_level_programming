#!/usr/bin/python3
"""MyList is subclass of list"""


class MyList(list):
    """MyList inherits list class"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
