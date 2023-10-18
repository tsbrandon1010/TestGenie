import unittest
import sys

def parse_result(result, retry_attempts, output_file):
    if result.returncode == 0:
        print(f'The generated unit test passed! \nSaving the file at: {output_file} \nExiting...')
        sys.exit()
    else:
        if retry_attempts == 0:
            print("The generated test failed, but user passed 0 for retry attempts.")
            print(f"Unit test has been saved to {output_file} \nExiting...")
            sys.exit()
        # test failed
        else:
            return False

class ParseResultTest(unittest.TestCase):

    def test_parse_result_success(self):
        class Result:
            returncode = 0
        result = Result()
        retry_attempts = 3
        output_file = 'test.txt'
        with self.assertRaises(SystemExit):
            parse_result(result, retry_attempts, output_file)
            
    def test_parse_result_retry_attempts_zero(self):
        class Result:
            returncode = 1
        result = Result()
        retry_attempts = 0
        output_file = 'test.txt'
        with self.assertRaises(SystemExit):
            parse_result(result, retry_attempts, output_file)
            
    def test_parse_result_failure(self):
        class Result:
            returncode = 1
        result = Result()
        retry_attempts = 3
        output_file = 'test.txt'
        self.assertFalse(parse_result(result, retry_attempts, output_file))
    
if __name__ == '__main__':
    unittest.main()