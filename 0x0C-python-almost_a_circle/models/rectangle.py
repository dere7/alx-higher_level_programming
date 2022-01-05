#!/usr/bin/python3
"""Defines Rectangle having width and height
"""
from .base import Base


class Rectangle(Base):
    """Defines Rectangle class having print_symbol and number_of_instance"""
    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle object
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        '''formal representation of Rectangle Object'''
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    @property
    def width(self):
        '''gets width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''sets width of the rectangle
        Args:
            width(int): width of the rectangle
        '''
        Base.integer_validator('width', width)
        self.__width = width

    @property
    def height(self):
        '''gets the height of the rectangle object'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height of the rectangle
        Args:
            value(int): height of the rectangle
        '''
        Base.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        '''gets the x of the rectangle object'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets x of the rectangle
        Args:
            value(int): height of the rectangle
        '''
        Base.integer_validator('x', value, True)
        self.__x = value

    @property
    def y(self):
        '''gets the y of the rectangle object'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets y of the rectangle
        Args:
            value(int): height of the rectangle
        '''
        Base.integer_validator('y', value, True)
        self.__y = value

    def __str__(self):
        """dispalys a rectange using #"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - ' \
               f'{self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """updates attributes of Rectangle"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        '''returns the area of the rectangle'''
        return self.height * self.width

    def display(self):
        """str represenation of Rectangle Object"""
        string = ''
        for i in range(self.y):
            string += '\n'

        for i in range(self.height):
            for k in range(self.x):
                string += ' '
            for j in range(self.width):
                string += str(self.print_symbol)
            string += '\n' if self.width != 0 and i + 1 != self.height else ''
        print(string)
