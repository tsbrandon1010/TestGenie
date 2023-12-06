
import unittest
from test import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
        
    def test_subtract(self):
        result = subtract(5, 2)
        self.assertEqual(result, 3)
        
    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)
        
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
            
    def test_invalid_operator(self):
        # Redirect stdout to check the printed message
        import sys
        from io import StringIO
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Simulate user input of invalid operator
        variable_one = 2
        variable_two = 3
        operator = "@"
        
        # Call the main logic of the program
        match operator:
            case "+":
                add(variable_one, variable_two)
            case "-":
                subtract(variable_one, variable_two)
            case "*":
                multiply(variable_one, variable_two)
            case "/":
                divide(variable_one, variable_two)
            case _:
                print("You did not enter a valid operator...")
        
        # Assert that the correct message is printed
        self.assertEqual(captured_output.getvalue().strip(), "You did not enter a valid operator...")
        
        # Reset stdout
        sys.stdout = sys.__stdout__
            
            
if __name__ == "__main__":
    unittest.main()
