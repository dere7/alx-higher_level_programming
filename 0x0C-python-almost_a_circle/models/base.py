#!/usr/bin/python3
"""
contains a base class that manages id attribute to remove
unnecessary redundancy.
"""
import json
import csv


class Base:
    """base of all other :classes in this project. It
    manages id attribute in all classes and to avoid duplicating
    the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def integer_validator(name, value, isGreaterThanOrEqual=False):
        """Validates integer
        :raises: TypeError
        :raises: ValueError"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0 and not isGreaterThanOrEqual:
            raise ValueError(f'{name} must be > 0')
        if isGreaterThanOrEqual and value < 0:
            raise ValueError(f'{name} must be >= 0')

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSON repr of list_dictionaries'''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string repr of list_objs to a file
        :arg
        :param list_objs: list of instances who inherits of Base"""
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(
                Base.to_json_string([obj.to_dictionary() for obj in list_objs]
                                    if list_objs is not None else []))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of JSON string repr json_string"""
        return json.loads(json_string) if json_string is not None else []

    @classmethod
    def create(cls, **dictionary):
        """creates an instance with all attributes already set"""
        if 'size' in dictionary:
            obj = cls(1)
        else:
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """loads list of instances from files"""
        try:
            with open(cls.__name__ + '.json') as f:
                list_objs = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dic) for dic in list_objs]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves csv to a file"""
        with open(cls.__name__ + '.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, cls.get_fields(),
                                    quoting=csv.QUOTE_MINIMAL)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def get_fields(cls):
        fieldnames = ['id', 'x', 'y']
        if cls.__name__ == 'Square':
            fieldnames.insert(1, 'size')
        else:
            fieldnames.insert(1, 'width')
            fieldnames.insert(2, 'height')
        return fieldnames

    @classmethod
    def load_from_file_csv(cls):
        """deserializes csv from file"""
        try:
            with open(cls.__name__ + '.csv', newline='') as f:
                reader = csv.DictReader(f, cls.get_fields())
                return [cls.create(**row) for row in reader]
        except FileNotFoundError:
            return []
