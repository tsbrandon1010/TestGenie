import unittest

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

class TestIsPrime(unittest.TestCase):
    
    def test_is_prime_positive(self):
        self.assertTrue(is_prime(2), "2 is prime")
        self.assertTrue(is_prime(3), "3 is prime")
        self.assertTrue(is_prime(5), "5 is prime")
        self.assertTrue(is_prime(7), "7 is prime")
        self.assertTrue(is_prime(11), "11 is prime")
    
    def test_is_prime_negative(self):
        self.assertFalse(is_prime(1), "1 is not prime")
        self.assertFalse(is_prime(4), "4 is not prime")
        self.assertFalse(is_prime(6), "6 is not prime")
        self.assertFalse(is_prime(8), "8 is not prime")
        self.assertFalse(is_prime(9), "9 is not prime")
    
    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0), "0 is not prime")
    
    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-1), "-1 is not prime")
        self.assertFalse(is_prime(-4), "-4 is not prime")
        self.assertFalse(is_prime(-6), "-6 is not prime")
        self.assertFalse(is_prime(-8), "-8 is not prime")
    
    def test_is_prime_large_numbers(self):
        self.assertTrue(is_prime(524287), "524287 is prime")
        self.assertFalse(is_prime(82589932), "82589933 is not prime")
    
unittest.main()