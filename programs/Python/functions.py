#NF
import math
def is_prime(num: int) -> bool:
    '''Check if a number (num) is prime or not.'''
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

'''
Usage:

print(is_prime(3))
> True

print(is_prime(10))
> False

'''

#NF
def factorial(num):
    '''Return the factorial of a given number (num)'''
    if num < 0:
        raise ValueError("Cannot find the factorial of a negaive number")
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

'''
Usage: 

print(factorial(2))
> 2

print(factorial(5))
> 120

'''

#NF
def add(a, b):
    '''Add two numbers'''
    return a + b

#NF
def subtract(a, b):
    '''Subtract two numbers'''
    return a - b

#NF
def multiply(a, b):
    '''Multiply two numbers'''
    return a * b

#NF
def divide(a, b):
    '''Divide two numbers'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b