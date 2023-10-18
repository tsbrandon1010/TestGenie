import unittest

def create_prompt(input_file): 
    prompt = f"""Write a unit test using unittest for the following program. Aim for 100% test coverage. Put each test case in its own test function.\nMake sure to define each function being unit tested in the python file (do not import the function being tested):\n\n{input_file}\n"""
    return prompt

class TestCreatePrompt(unittest.TestCase):

    def test_create_prompt(self):
        # Test Case 1: Check with an ordinary string as input_file
        input_file = "Test File"
        expected_output = f"""Write a unit test using unittest for the following program. Aim for 100% test coverage. Put each test case in its own test function.\nMake sure to define each function being unit tested in the python file (do not import the function being tested):\n\n{input_file}\n"""
        self.assertEqual(create_prompt(input_file), expected_output)

        # Test Case 2: Check with blank string as input_file
        input_file = ""
        expected_output = f"""Write a unit test using unittest for the following program. Aim for 100% test coverage. Put each test case in its own test function.\nMake sure to define each function being unit tested in the python file (do not import the function being tested):\n\n\n"""
        self.assertEqual(create_prompt(input_file), expected_output)

        # Test Case 3: Check with special characters as input_file
        input_file = "#$%^&*()"
        expected_output = f"""Write a unit test using unittest for the following program. Aim for 100% test coverage. Put each test case in its own test function.\nMake sure to define each function being unit tested in the python file (do not import the function being tested):\n\n{input_file}\n"""
        self.assertEqual(create_prompt(input_file), expected_output)


if __name__ == '__main__':
    unittest.main()
