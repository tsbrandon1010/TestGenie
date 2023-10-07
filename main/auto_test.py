import subprocess
import re
import sys
import openai
import os
from halo import Halo
import click
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


"""

    python auto_test.py -i programs/prime-checker/main/is-prime.py -o programs/prime-checker/test/is-prime.py -r 1

"""
@click.command()
@click.option('-i', '--input', help='The input file to the program you would like to create unit tests for', required=True)
@click.option('-o', '--output', help='The output file where you would like to save the resulting unit test', required=True)
@click.option('-r', '--retry-attempts', type=click.IntRange(0, 3, clamp=True), default=0, help='The number of times you would like the tool to retry generating a unit test if the generated test fails', required=False)
@click.option('-t', '--test', is_flag=True, help='Include this flag if you want your unit-test tested for you')
def generate_test(input, output, retry_attempts, test):
        
    print(test)    

    # need to add a check that the file exists, or use the build in click path/file type
    with open(input, 'r') as f:
        lines = f.readlines()

    input_file = ""
    for line in lines:
        input_file += line

    prompt = f"""
    Write a unit test using unittest for the following function. Aim for 100% coverage. Put each test case in its own test function, you may have multiple tests per test case. 
    Make sure to define each function being unit tested in the python file (do not import the function): 

    {input_file}
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
    with open(output, 'w') as f:
        f.write(response_text)

    if not test:
        print(f'Your test was generated, but not run. \nExiting...')
        sys.exit()

    unit_test_output = subprocess.run(['python', output], capture_output=True, check=False)
    if unit_test_output.returncode == 0:
        print(f'The generated unit test passed! \nSaving the file at: {output} \nExiting...')
        sys.exit()
    else:
        test_fails = True
        if retry_attempts == 0:
            print("The generated test failed, but user passed 0 for retry attempts.")
            print(f"Unit test has been saved to {output} \nExiting...")
            sys.exit()


    # generate new unit tests while the test fails and we have not exceeded our retry attempts
    current_retry_attempts = 1
    while test_fails == True and current_retry_attempts <= retry_attempts: 
        print(f"The generated test failed, retrying...\nRetry Attempts: {current_retry_attempts}")
        
        unit_test = ""
        with open(output, 'r') as f:
            line = f.readlines()
        for line in lines:
            unit_test += line
        
        prompt = f"""
        This unit test:
        {unit_test}

        For the following file:
        {input_file}        

        Ran with the following errors:
        {unit_test_output.stderr}

        Re-write the unit test so that it is absent of errors. Make sure to include the function definition for every function that is being unit tested.
        """

        spinner.start()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt}. Only respond with code as plain text."}]
        )
        spinner.stop()

        response_text = re.split('```python | ```', response['choices'][0]['message']['content'])[0]
        with open(output, 'w') as f:
            f.write(response_text)

        unit_test_output = subprocess.run(['python', output], capture_output=True, check=False)
        if unit_test_output.returncode == 0:
            print('The generated unit test passed! \nExiting...')
            sys.exit()
        else:
            test_fails = True
            current_retry_attempts += 1

    print(f"A passing unit test could not be found in the allotted number of retry attempts: {retry_attempts}")
    print(f"Unit test has been saved at: {output} \nExiting...")

if __name__ == "__main__":
    generate_test()