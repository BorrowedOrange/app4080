import unittest

# Define the factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Define the square calculation function
def calculate_square(number):
    return number ** 3

# Create a test class that inherits from unittest.TestCase
class TestFactorialAndSquareFunctions(unittest.TestCase):

    # Test cases for the factorial function
    def test_factorial(self):
        # Test for the factorial of 0
        self.assertEqual(factorial(0), 1)
        
        # Test for the factorial of 1
        self.assertEqual(factorial(1), 1)
        
        # Test for the factorial of 5
        self.assertEqual(factorial(5), 120)
        
        # Test for the factorial of 10
        self.assertEqual(factorial(10), 3628800)

    # Test cases for the square calculation function
    def test_calculate_square(self):
        # Test for the square of 0
        self.assertEqual(calculate_square(0), 0)
        
        # Test for the square of 1
        self.assertEqual(calculate_square(1), 1)
        
        # Test for the square of 5
        self.assertEqual(calculate_square(5), 25)
        
        # Test for the square of a negative number (-5)
        self.assertEqual(calculate_square(-5), 25)

# Entry point to run the tests
if __name__ == '__main__':
    unittest.main()
