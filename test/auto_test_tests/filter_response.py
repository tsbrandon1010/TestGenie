import unittest
import re

def filter_response(response):
    if len(response['choices']) == 0:
        return None
    
    filtered_response = re.findall('```python\n(.*?)\n```', response['choices'][0]['message']['content'])
    return filtered_response[0]

class TestFilterResponse(unittest.TestCase):
    def test_filter_response_first_choice(self):
        response = {
            'choices': [{
                'message': {
                    'content': '```python\nfiltered code 1\n```'
                }
            }]
        }
        expected_output = 'filtered code 1'
        
        self.assertEqual(filter_response(response), expected_output)
        
    def test_filter_response_multiple_choices(self):
        response = {
            'choices': [
                {
                    'message': {
                        'content': '```python\nfiltered code 1\n```'
                    }
                },
                {
                    'message': {
                        'content': '```python\nfiltered code 2\n```'
                    }
                }
            ]
        }
        expected_output = 'filtered code 1'
        
        self.assertEqual(filter_response(response), expected_output)
        
    def test_filter_response_no_choices(self):
        response = {
            'choices': []
        }
        expected_output = None
        
        self.assertEqual(filter_response(response), expected_output)

if __name__ == '__main__':
    unittest.main()