#!/usr/bin/python3
'''Defines Rectangle having width and height
'''


class Rectangle:
    '''Defines Rectange class having print_symbol and number_of_instance'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initializes Rectangle object
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        '''some cleanups when the object is destoryed'''
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    def __str__(self):
        '''str represenation of Rectangle Object'''
        string = ''
        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            string += '\n' if self.width != 0 and i + 1 != self.height else ''
        return string

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
