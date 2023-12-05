import unittest

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
        self.assertFalse(is_prime(82589933), "82589933 is not prime")
    
    def test_is_prime_float(self):
        self.assertFalse(is_prime(2.5), "2.5 is not prime")
        self.assertFalse(is_prime(3.14), "3.14 is not prime")
    
    def test_is_prime_string(self):
        self.assertFalse(is_prime("5"), "string '5' is not prime")
        self.assertFalse(is_prime("hello"), "string 'hello' is not prime")

unittest.main() 