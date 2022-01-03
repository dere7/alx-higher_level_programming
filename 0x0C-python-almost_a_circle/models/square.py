#!/usr/bin/python3
"""defines square class from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """subclass of Rectangle with attributes size"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) != 0:
            ls = list(args)
            ls.insert(1, args[1]) if len(args) >= 2 else None
            ls = tuple(ls)
            super().update(*ls)
        else:
            size = kwargs.get('size')
            if size is not None:
                kwargs['width'] = size
                kwargs['height'] = size
        super().update(**kwargs)
