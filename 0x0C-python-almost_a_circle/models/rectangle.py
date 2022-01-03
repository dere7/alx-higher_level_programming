#!/usr/bin/python3
"""Defines Rectangle having width and height
"""
from .base import Base


class Rectangle(Base):
    """Defines Rectange class having print_symbol and number_of_instance"""
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

    # def __del__(self):
    #     """some cleanups when the object is destoryed"""
    #     print('Bye rectangle...')

    def __repr__(self):
        '''formal represenation of Rectangle Object'''
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

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''compares two Rectangle objects
        Args:
            rect_1(Rectangle): object of Rectangle class
            rect_2(Rectangle): object of Rectangle class
        Return: rect_1 if the area of rect_1 is greater than or
                equal to rect_2 otherwise return rect_2
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """create square using Rectangle
        Args:
            cls:
            size: size of square
        """
        return cls(size, size)
