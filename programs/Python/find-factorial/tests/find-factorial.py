import unittest

def factorial(num):
    '''Return the factorial of a given number (num)'''
    if num < 0:
        raise ValueError("Cannot find the factorial of a negative number")
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)        

class TestFactorial(unittest.TestCase):

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
        
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)
            
    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)
        
    def test_factorial_decimal(self):
        with self.assertRaises(ValueError):
            factorial(3.5)
            
    def test_factorial_string_input(self):
        with self.assertRaises(TypeError):
            factorial("abc")
            

if __name__ == '__main__':
    unittest.main()