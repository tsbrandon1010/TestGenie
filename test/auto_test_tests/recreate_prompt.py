import unittest

def recreate_prompt(failed_test, failed_test_result, input_file):
    prompt = f"""
    This unit test:
    {failed_test}

    For the following file:
    {input_file}       

    Ran with the following errors:
    {failed_test_result}

    Re-write the unit test so that it is absent of errors. Make sure to include the function definition for every function that is being unit tested.
    """
    return prompt


class TestRecreatePrompt(unittest.TestCase):

    def test_recreate_prompt(self):
        failed_test = 'TestAdd'
        failed_test_result = 'err'
        input_file = 'test_file.py'
        
        expected_output = f"""
        This unit test:
        {failed_test}

        For the following file:
        {input_file}       

        Ran with the following errors:
        {failed_test_result}

        Re-write the unit test so that it is absent of errors. Make sure to include the function definition for every function that is being unit tested.
        """
        self.assertEqual(recreate_prompt(failed_test, failed_test_result, input_file), expected_output)


if __name__ == '__main__':
    unittest.main()
