import unittest

class TestIsPrime(unittest.TestCase):
    
    # Test for prime numbers
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
    
    # Test for non-prime numbers
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(27))
        self.assertFalse(is_prime(30))
    
    # Test for negative numbers
    def test_negative_numbers(self):
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-11))
        self.assertFalse(is_prime(-13))
        self.assertFalse(is_prime(-17))
        self.assertFalse(is_prime(-19))
        self.assertFalse(is_prime(-23))
        self.assertFalse(is_prime(-29))
    
    # Test for large prime numbers
    def test_large_prime_numbers(self):
        self.assertTrue(is_prime(7919))
        self.assertTrue(is_prime(15485863))
        self.assertTrue(is_prime(2147483647))
    
    # Test for large non-prime numbers
    def test_large_non_prime_numbers(self):
        self.assertFalse(is_prime(7907))
        self.assertFalse(is_prime(15485763))
        self.assertFalse(is_prime(2147483641))

if __name__ == '__main__':
    unittest.main()