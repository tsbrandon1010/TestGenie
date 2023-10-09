import openai
import json
# Just create the interface and allow the MockAPI and OpenAI tests to define their own versions of generate prompt?

"""
    auto_test.py Use Case:
        User has a program like: /programs/prime-checker/main/is-prime.py
        All they need to do is input their program into the test generator and save the generated test
            Usage:
            - auto_test -i /programs/prime-checker/main/is-prime.py -o /programs/prime-checker/test/is-prime.py

        Under the hood:
            - A prompt is generated from the function that they pass
            - An LLM is prompted with the generated prompt to create a unit-test for the function
            - Response is received
            - OUTSIDE OF APICaller:
                * The response is written to a file and tested, if the test fails we repeat the above steps until a valid test is generated or max retries is reached

    MockAPI_tests.py Use Case:
        When running MockAPI_tests.py, it will run through 3 cases on fake output data 
            3 Tests (using is-prime.py ?) where:
            - Test fails on the first time and is not re-prompted and retested
            - Test passes the first time
            - Tests fails the first time and then passes after a re-prompt and test

       
    OpenAIAPI_tests.py Use Case:
        Similar to MockAPI_tests.py:
            3 Tests (using is-prime.py ?) using real OpenAi api calls where:
            - Test fails on the first time and is not re-prompted and retested
            - Test passes the first time
            - Tests fails the first time and then passes after a re-prompt and test

"""

class ApiCallerInterface:
    def query():
        pass

"""
    We want the mock api caller to respond to queries with the fake outputs that we made. 
    It can either pull queries from ./test/MockApiTests/Test1, ./test/MockApiTests/Test2, or ./test/MockApiTests/Test3
        - how do we indicate which folder we want to pull from?
    If we pull from a folder that has multiple outputs, it still needs to test the output, run it, and get another "query" if it fails

"""
class MockApiCaller(ApiCallerInterface):
    def __init__(self):
        pass

    # case = (test #, retry #)
    def query(self, test_case): 
        match test_case[0]:
            case 1:
                response_file =  "../test/MockApiTests/test1/mock_api_output_test_1.txt"
            case 2:
                if test_case[1] == 0:
                    response_file = "../test/MockApiTests/test2/mock_api_output_test_1.txt"
                else:
                    response_file = "../test/MockApiTests/test2/mock_api_output_test_2.txt"
            case 3:
                if test_case[1] == 0:
                    response_file = "../test/MockApiTests/test3/mock_api_output_test_1.txt"
                elif test_case[1] == 1:
                    response_file = "../test/MockApiTests/test3/mock_api_output_test_2.txt"
                else:
                    response_file = "../test/MockApiTests/test3/mock_api_output_test_3.txt"

        response = {}
        with open(response_file, 'r') as f:
            json.load(f)
        
        return response

class OpenAiApiCaller(ApiCallerInterface):
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    def query(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": f"{prompt}. Only respond with code as plain text."}]
        ) 
        return response