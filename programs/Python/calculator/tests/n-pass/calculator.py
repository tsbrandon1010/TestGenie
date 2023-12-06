import unittest

def add(a, b):
    '''Add two numbers'''
    return a + b

def subtract(a, b):
    '''Subtract two numbers'''
    return a - b

def multiply(a, b):
    '''Multiply two numbers'''
    return a * b

def divide(a, b):
    '''Divide two numbers'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = multiply(5, 10)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = divide(10, 5)
        self.assertEqual(result, 2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()