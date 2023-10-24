import subprocess
import ast
import re
import sys
from halo import Halo
import click
from APICaller import OpenAiApiCaller

def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    return lines

# need to add a check that the file exists, or use the build in click path/file type
def create_prompt(input_file): 
    prompt = f"""
    Write a unit test for the following program. Aim for 100% test coverage. Put each test case in its own test function. 
    Make sure to define each function being unit tested in the file (do not import the function being tested): 

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

def filter_response(response, language):
    
    # csharp
    if language == 'python':
        lang = 'python'
    elif language.lower() == 'c#':
        lang = 'csharp'
    
    filtered_response = re.split(f'```{lang}|```', response['choices'][0]['message']['content'])
    
    if len(filtered_response) == 1:
        return filtered_response[0]
    else:
        return filtered_response[1]

def run_test(response, output_file, language):
    with open(output_file, 'w') as f:
        f.write(response)
    
    if language.lower() == 'python':
        unit_test_output = subprocess.run(['python', output_file], capture_output=True, check=False)
    elif language.lower() == 'c#':
        unit_test_output = subprocess.run(['csc', output_file], capture_output=True, check=False)
    
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

def extract_imports(parsed_ast):
    imports = []
    for node in ast.walk(parsed_ast):
        if type(node) == ast.Import or type(node) == ast.ImportFrom:
            imports.append(node.lineno - 1)

    return imports

def extract_functions(parsed_ast):
    functions = []
    for node in ast.walk(parsed_ast):
        if type(node) == ast.FunctionDef:
            
            func_range = (node.lineno - 1, node.end_lineno)
            functions.append(func_range)

    return functions


@click.command()
@click.option('-i', '--input-file', help='The input file to the program you would like to create unit tests for', required=True)
@click.option('-o', '--output-file', help='The output file where you would like to save the resulting unit test', required=True)
@click.option('-r', '--retry-attempts', type=click.IntRange(0, 3, clamp=True), default=0, help='The number of times you would like the tool to retry generating a unit test if the generated test fails', required=False)
@click.option('-l', '--language', type=click.Choice(['python', 'C#'], case_sensitive=False), help='The language of the file for which tests are being generated')
@click.option('-s', '--sparse', is_flag=True, default=False, help='Include this flag if you want to test a specific unit')
def generate_test(input_file, output_file, retry_attempts, language, sparse):
        
    if sparse:
        if language.lower() == 'c#':
            SystemExit("C# is not currently supported for sparse test generation. \nExiting...")
        
        content = read_file(input_file)
        parsed_ast = ast.parse("".join(content))

        imports = extract_imports(parsed_ast)
        functions = extract_functions(parsed_ast)

        print("Which functions would you like to write tests for? ", end="")
        print("If multiple, seperate with a comma: \nExample: 1, 2, 4")
        for j, i in enumerate(functions):
            print(f"{j + 1}: (line {i[0]})", content[i[0]])

        user_input = input("> ").split(',')

        for i in imports:
            input_file += content[i]

        selected_functions = []
        for i in user_input:
            print(i)
            try:
                if int(i) > 0 and int(i) - 1 < len(functions):
                    selected_functions.append(int(i))
            except:
                pass

        print(f"Generating tests for: \n{selected_functions}")
        usr_continue = input("Would you like to continue? [Y/n] \n> ")
        if usr_continue.lower() != 'y':
            sys.exit()

        input_file = ""
        for i in selected_functions:
            input_file += "".join(content[functions[i - 1][0]:functions[i - 1][1]])

    else:
        lines = read_file(input_file)

        input_file = "" 
        for line in lines:
            input_file += line

    print(input_file)


    spinner = Halo(text='Generating Unit Test...', spinner='dots')
    spinner.start()
    prompt = create_prompt(input_file)    
    apiCaller = OpenAiApiCaller(model='gpt-3.5-turbo')
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