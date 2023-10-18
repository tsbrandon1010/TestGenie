import re

def filter_response(response):
    filtered_response = re.split('```python|```', response['choices'][0]['message']['content'])    
    return filtered_response[1]