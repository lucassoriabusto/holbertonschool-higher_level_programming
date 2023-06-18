#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


# Test class definition
class TestMaxInteger(unittest.TestCase):

    # Test method for max_integer
    def test_max_integer(self):

        # Test case: empty list
        self.assertEqual(max_integer([]), None)

        # Test case: list with a single element
        self.assertEqual(max_integer([7]), 7)

        # Test case: list with a single negative element
        self.assertEqual(max_integer([-7]), -7)

        # Test case: list with negative elements
        self.assertEqual(max_integer([-1, -5, -3]), -1)

        # Test case: list with positive elements
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

        # Test case: list with positive and negative elements
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)

        # Test case: list with equal elements
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)


if __name__ == '__main__':
    unittest.main()
