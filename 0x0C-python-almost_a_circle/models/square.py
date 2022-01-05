#!/usr/bin/python3
"""defines square class from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """subclass of Rectangle with attributes size"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string repr of square"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter
        :arg
        :param value: int"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates squares id, size, x and y
        :arg
            :param args: variable length arg
            :param kwargs: key value pair of parameters
        """
        if len(args) != 0:
            ls = list(args)
            ls.insert(1, args[1]) if len(args) >= 2 else None
            ls = tuple(ls)
            super().update(*ls)
        else:
            size = kwargs.get('size')
            if size is not None:
                del kwargs['size']
                kwargs['width'] = size
                kwargs['height'] = size
            super().update(**kwargs)
