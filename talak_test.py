import unittest
from week9 import factorial, square

class TestFunctions(unittest.TestCase):

  def test_factorial(self):
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(1), 1) 
    self.assertEqual(factorial(5), 120)
    self.assertEqual(factorial(10), 3628800)

  def test_square(self):
    self.assertEqual(square(2), 4.0)
    self.assertEqual(square(5), 25.0)
    self.assertEqual(square(-3), 9.0)
    self.assertEqual(square(0), 0.0)

if __name__ == '__main__':
  unittest.main()