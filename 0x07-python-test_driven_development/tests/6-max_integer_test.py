#!/usr/bin/python3
'''Unittest for max_integer([...])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Test case for max-integer'''
    def test_max_integer(self):
        '''tests max_integer '''
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 5, 32, 4]), 32)
        self.assertEqual(max_integer([34, 22, 343, 22, 22]), 343)
        self.assertEqual(max_integer([3]), 3)
