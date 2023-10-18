import unittest
import tempfile
import os

def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    file = ""
    for line in lines:
        file += line

    return file

class TestReadFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.gettempdir()
        self.test_file = os.path.join(self.test_dir, 'test_file.txt')
        with open(self.test_file, 'w') as f:
            f.write("Hello\nWorld")

    def test_read_file(self):
        expected_output = "Hello\nWorld"
        actual_output = read_file(self.test_file)
        self.assertEqual(actual_output, expected_output)

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

if __name__ == '__main__':
    unittest.main()
