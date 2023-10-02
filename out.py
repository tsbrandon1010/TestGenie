import math
import unittest
def is_prime(num: int) -> bool:
    '''Check if a number (num) is prime or not.'''    
    for i in range(2,int(math.sqrt(num))+1):       
        if num%i==0:            
            return False   
    return True
    
class TestIsPrime(unittest.TestCase):    
    def test_prime_number(self):        
        self.assertTrue(is_prime(3))   
        
    def test_non_prime_number(self):       
        self.assertFalse(is_prime(10))
        
        if __name__ == '__main__':    
            unittest.main()