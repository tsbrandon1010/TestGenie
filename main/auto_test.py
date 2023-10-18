import subprocess
import re
import sys
from halo import Halo
import click
from APICaller import OpenAiApiCaller

def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    file = ""
    for line in lines:
        file += line

    return file

# need to add a check that the file exists, or use the build in click path/file type
def create_prompt(input_file): 
    prompt = f"""
    Write a unit test using unittest for the following program. Aim for 100% test coverage. Put each test case in its own test function. 
    Make sure to define each function being unit tested in the python file (do not import the function being tested): 

    {input_file}
    """

    return prompt

def recreate_promt(failed_test, failed_test_result, input_file):
    prompt = f"""
    This unit test:
    {failed_test}

    For the following file:
    {input_file}        

    Ran with the following errors:
    {failed_test_result.stderr}

    Re-write the unit test so that it is absent of errors. Make sure to include the function definition for every function that is being unit tested.
    """
    
    return prompt

def filter_response(response):
    filtered_response = re.split('```python|```', response['choices'][0]['message']['content'])    
    return filtered_response[1]

def run_test(response, output_file):
    with open(output_file, 'w') as f:
        f.write(response)
    
    unit_test_output = subprocess.run(['python', output_file], capture_output=True, check=False)
    return unit_test_output

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


@click.command()
@click.option('-i', '--input-file', help='The input file to the program you would like to create unit tests for', required=True)
@click.option('-o', '--output-file', help='The output file where you would like to save the resulting unit test', required=True)
@click.option('-r', '--retry-attempts', type=click.IntRange(0, 3, clamp=True), default=0, help='The number of times you would like the tool to retry generating a unit test if the generated test fails', required=False)
def generate_test(input_file, output_file, retry_attempts):
        
    # need to add a check that the file exists, or use the build in click path/file type
    input_file = read_file(input_file)

    spinner = Halo(text='Generating Unit Test...', spinner='dots')
    spinner.start()
    prompt = create_prompt(input_file)
    apiCaller = OpenAiApiCaller(model='gpt-4')
    response = apiCaller.query(prompt)
    spinner.stop()

    filt_response = filter_response(response)

    # write the unit test to a python file. run it, if the tests fail re-prompt the LLM
    test_result = run_test(filt_response, output_file)
    parsed_result = parse_result(test_result, retry_attempts, output_file)

    current_retry_attempts = 0
    while parsed_result == False and current_retry_attempts < retry_attempts:
        print(f"The generated test failed, retrying...\nRetry Attempts: {current_retry_attempts}")
        current_retry_attempts += 1

        failed_test = read_file(output_file)

        spinner.start()
        prompt = recreate_promt(failed_test, test_result, input_file)
        response = apiCaller.query(prompt)
        spinner.stop()

        filt_response = filter_response(response)
        test_result = run_test(filt_response, output_file)
        parsed_result = parse_result(test_result, retry_attempts, output_file)

    print(f"A passing unit test could not be found in the allotted number of retry attempts: {retry_attempts}")
    print(f"Unit test has been saved at: {output_file} \nExiting...")

if __name__ == "__main__":
    generate_test()