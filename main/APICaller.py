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
    def generate_prompt():
        pass

    # calling query will query 
    def query():
        pass



    pass
