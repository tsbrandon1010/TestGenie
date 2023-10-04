import subprocess
import re
import sys
import openai
import os
from halo import Halo
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


"""
    First argument: path to the file that they want to write a unit test with
    Second argument: number of times the LLM will be re-prompted if the unit test fails 

    Example:

    python auto_test.py <function_to_test.py> <n_retries>
"""
def main():
    if len(sys.argv) < 3: 
        passed_args = [sys.argv[i] for i in range(1, len(sys.argv), 1)]
        print(f"An invalid number of arguments were passed: {passed_args} \nAborting...")
        sys.exit()
    else:
        if os.path.isfile(sys.argv[1]) and sys.argv[1].lower().endswith('.py'):
            user_inputed_file = sys.argv[1].lower()
        else:
            print(f"An invalid file/path was passed: {sys.argv[1]} \nAborting...")
            sys.exit()
        try:
            if int(sys.argv[2]) > 3:
                print(f"User inputted a value higher than the maximum allowed number of retries (3): {sys.argv[2]}")
                print("Defaulting to 3 retries...")
                user_inputted_retry_attempts = 3
            elif int(sys.argv[2]) < 0:
                print(f"User inputted a negative number of retries: {sys.argv[2]}")
                print("Defaulting to 0 retries...")
                user_inputted_retry_attempts = 0
            else:
                user_inputted_retry_attempts = int(sys.argv[2])
        except Exception as e:
            print(f"Number of retries may only be an integer: {sys.argv[2]} \nAborting...")
            sys.exit()
        

    with open(user_inputed_file, 'r') as f:
        lines = f.readlines()

    functions = [[] for line in lines if line == '#NF\n']

    counter = -1 
    for line in lines:
        if line == '#NF\n':
            counter += 1
            continue

        functions[counter].append(line)

    prompt = f"""

    Write a unit test using unittest for the following function. Aim for 100% coverage. Put each test case in its own test function, you may have multiple tests per test case. 
    Make sure to define the function being unit tested in the python file (do not import the function): 

    {functions[0]}

    """

    spinner = Halo(text='Generating Unit Test...', spinner='dots')
    spinner.start()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}. Only respond with code as plain text."}]

    )
    spinner.stop()


    # write the unit test to a python file. run it, if the tests fail re-prompt the LLM
    response_text = re.split('```python | ```', response['choices'][0]['message']['content'])[0]
    with open("generated_unit_test.py", 'w') as f:
        f.write(response_text)

    unit_test_output = subprocess.run(['python', './generated_unit_test.py'], capture_output=True, check=False)
    if unit_test_output.returncode == 0:
        print('The generated unit test passed! \nExiting...')
        sys.exit()
    else:
        test_fails = True
        if user_inputted_retry_attempts == 0:
            print("The generated test failed, but user passed 0 for retry attempts \nAborting... ")
            sys.exit()


    # generate new unit tests while the test fails and we have not exceeded our retry attempts
    retry_attempts = 1
    while test_fails == True and retry_attempts <= user_inputted_retry_attempts: 
        print(f"The generated test failed, retrying...\nRetry Attempts: {retry_attempts}")
        
        unit_test = ""
        with open("./generated_unit_test.py", 'r') as f:
            line = f.readlines()
        for line in lines:
            unit_test += line
        
        prompt = f"""

        This unit test:

        {unit_test}

        Ran with the following errors:

        {unit_test_output.stderr}


        Re-write the unit test so that it is absent of errors. Make sure to include the function definition for function that is being unit tested.

        """

        spinner.start()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt}. Only respond with code as plain text."}]
        )
        spinner.stop()

        response_text = re.split('```python | ```', response['choices'][0]['message']['content'])[0]
        with open("generated_unit_test.py", 'w') as f:
            f.write(response_text)

        unit_test_output = subprocess.run(['python', './generated_unit_test.py'], capture_output=True, check=False)
        if unit_test_output.returncode == 0:
            print('The generated unit test passed! \nExiting...')
            sys.exit()
        else:
            test_fails = True
            retry_attempts += 1

    print("A passing unit test could not be found in the allotted number of retry attempts... \nExiting...")

if __name__ == "__main__":
    main()