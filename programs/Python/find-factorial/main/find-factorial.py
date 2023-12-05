def factorial(num: int):
    '''Return the factorial of a given number (num)'''
    if num < 0:
        raise ValueError("Cannot find the factorial of a negative number")
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)