import unittest
from unittest.mock import patch, mock_open, call
import subprocess

def run_test(response, output_file):
    with open(output_file, 'w') as f:
        f.write(response)
    
    unit_test_output = subprocess.run(['python', output_file], capture_output=True, check=False)
    return unit_test_output

class TestRunTest(unittest.TestCase):
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_run_test(self, mock_file, mock_subprocess):
        response = 'test response'
        output_file = 'test.py'
        expected_output = subprocess.CompletedProcess(args='completed', returncode=0)
        mock_subprocess.return_value = expected_output

        actual_output = run_test(response, output_file)

        self.assertEqual(actual_output, expected_output)
        mock_file.assert_called_once_with(output_file, 'w')
        mock_file().write.assert_called_once_with(response)

        python_execution_call = call(['python', output_file], capture_output=True, check=False)
        mock_subprocess.assert_has_calls([python_execution_call])

if __name__ == '__main__':
    unittest.main()
