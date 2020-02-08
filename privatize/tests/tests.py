"""
tests.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

import numpy as np
from privatize import privatize
import sys
import unittest


# Class to test out privatize
class TestClass:
    x = privatize(dtype='int')
    y = privatize(dtype='str', immutable=True)

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Unit tests
class TestPrivatize(unittest.TestCase):
    def test_assignment(self):
        test = TestClass(6, 'A')

        np.testing.assert_equal(test.x, 6)
        np.testing.assert_equal(test.y, 'A')

        test.x = 7

        np.testing.assert_equal(test.x, 7)
        np.testing.assert_equal(test.y, 'A')

        # And we can test if another object is created, that we can store their separate values
        test2 = TestClass(8, 'A')

        np.testing.assert_equal(test.x, 7)
        np.testing.assert_equal(test2.x, 8)

    def test_immutable(self):
        test = TestClass(6, 'A')

        # If we try to set y again, we will get an AttributeError
        with np.testing.assert_raises(AttributeError):
            test.y = 'B'

    def test_fixed_dtype(self):
        test = TestClass(6, 'A')

        # And if we try to set x with anything but an int, we'll get an AttributeError
        with np.testing.assert_raises(AttributeError):
            test.x = 'hey'


# Test cases
test_cases = [
    TestPrivatize
]


# Function to run tests
def test():
    # Create a test suite
    suite = unittest.TestSuite()

    # Load all our test cases into the suite
    loader = unittest.TestLoader()
    for test_case in test_cases:
        suite.addTests(loader.loadTestsFromTestCase(test_case))

    # Create test runner and run
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # If the test was not successful, exit with a code
    if not result.wasSuccessful():
        sys.exit(1)



