import math
import unittest

def is_prime(num: int) -> bool:
    '''Check if a number (num) is prime or not.'''
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        # Test case where num is prime
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(11), True)
        
        # Test case where num is not prime
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(8), False)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(10), False)
        
        # Test case where num is negative
        self.assertEqual(is_prime(-2), False)
        self.assertEqual(is_prime(-3), False)
        self.assertEqual(is_prime(-5), False)
        self.assertEqual(is_prime(-7), False)
        self.assertEqual(is_prime(-11), False)
        
        # Test case where num is 0 or 1
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)

if __name__ == '__main__':
    unittest.main()