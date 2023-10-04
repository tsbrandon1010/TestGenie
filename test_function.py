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