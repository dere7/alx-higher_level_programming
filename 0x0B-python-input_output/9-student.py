#!/usr/bin/python3
"""
defines a student
"""


class Student:
    """
    defines a student with attributes first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes Student object
        :param first_name: first name of Student obj
        :param last_name: last name of Student obj
        :param age: age of Student obj
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        dictionary repr of Students instance
        :return: dict of Student object
        """
        return vars(self)
