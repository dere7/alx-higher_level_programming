#!/usr/bin/python3
'''Defines Rectangle having width and height
'''


class Rectangle:
    '''Defines Rectange class having print_symbol and number_of_instance'''
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initializes Rectangle object
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            '''
        self.width = width
        self.height = height

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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        '''gets the height of the rectangle object'''
        return self.__height

    @height.setter
    def height(self, height):
        '''sets height of the rectangle
        Args:
            height(int): height of the rectangle
        '''
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        '''returns the area of the rectangle'''
        return self.height * self.width

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)