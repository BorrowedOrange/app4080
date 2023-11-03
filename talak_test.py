import unittest 

class TestFunctions(unittest.TestCase):
  
    # Test factorial function
    def test_factorial(self):
        # Factorial of 0 is 1
        self.assertEqual(factorial(0), 1)  
        # Factorial of 1 is 1
        self.assertEqual(factorial(1), 1)
        # Factorial of 5 is 120
        self.assertEqual(factorial(5), 120)
        # Factorial of 10 is 3628800
        self.assertEqual(factorial(10), 3628800)
    
    # Test square function  
    def test_square(self):
        # Square of 2 is 4
        self.assertEqual(square(2), 4) 
        # Square of 5 is 25
        self.assertEqual(square(5), 25)
        # Square of -3 is 9
        self.assertEqual(square(-3), 9) 
        # Square of 0 is 0
        self.assertEqual(square(0), 0)
        
if __name__ == '__main__':
    unittest.main()