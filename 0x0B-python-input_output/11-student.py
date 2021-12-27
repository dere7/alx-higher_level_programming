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

    def to_json(self, attrs=None):
        """
        dictionary repr of Students instance
        :return: dict of Student object
        """
        dic = vars(self)
        if attrs is None:
            return dic
        for i in list(dic.keys()):
            if i not in attrs:
                del dic[i]
        return dic.copy()

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        :param json: dict
        :return: None
        """
        for key in json.keys():
            setattr(self, key, json[key])
