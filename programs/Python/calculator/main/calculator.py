def add(a, b):
    '''Add two numbers'''
    return a + b

def subtract(a, b):
    '''Subtract two numbers'''
    return a - b

def multiply(a, b):
    '''Multiply two numbers'''
    return a * b

def divide(a, b):
    '''Divide two numbers'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    operations = "+ <-- add \n- <-- subtract \n* <-- multiply \n/ <-- divide\n"
    running = True
    while running:
        operator = input("Enter your operation:\n" + operations + "> ")
        variable_one = input("Enter the first variable: \n> ")
        variable_two = input("Enter the second variable: \n> ")

        match operator:
            case "+":
                print(f"Result: {add(variable_one, variable_two)}\n")
            case "-":
                print(f"Result: {subtract(variable_one, variable_two)}\n")
            case "*":
                print(f"Result: {multiply(variable_one, variable_two)}\n")
            case "/":
                print(f"Result: {divide(variable_one, variable_two)}\n")
            case _:
                print("You did not enter a valid operator...\n")