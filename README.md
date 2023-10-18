# LLM-Unit-Tests
 
## Getting Started:

Assuming that you have a supported Python installation (3.x), you can start by 
cloning the repository:
```
git clone https://github.com/tsbrandon1010/LLM-Unit-Tests
```
Or by downloading the repository as a ZIP file:

![image](https://github.com/tsbrandon1010/LLM-Unit-Tests/assets/15933213/efc1e196-8241-42e2-a369-0fa743dc5d25)


Next, we can get the required packages:

```
pip install -r requirements.txt
```

### Using the tool
After downloading the tool and package dependencies, you must create an API key with [OpenAI](https://openai.com/).
<br>More information can be found ***[here](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0)***.

![Screenshot 2023-10-18 122012](https://github.com/tsbrandon1010/LLM-Unit-Tests/assets/15933213/e079c7ad-2e7c-4ced-add5-457aecf3e68f)

Within the ```~/LLM-Unit-Tests/main``` directory, there is a file called ```.env```. This is where you will put your OpenAI API key (your key will go within the quotations).

![image](https://github.com/tsbrandon1010/LLM-Unit-Tests/assets/15933213/9ac8d712-a72f-4690-8341-2f2ddca2c4e9)

We should now be able to use the tool:
<br>```python auto_test.py -i <input> -o <output> -r <max retries>```

```-i```: The path of the file for which the tool will generate a unit test.
<br>```-o```: A path to the file where the generated unit test will be saved.
<br>```-r```: The maximum number of times to re-generate the unit test if the test fails.

### Running through examples
There is an example program we are going to use called ```is-prime.py``` that is located in ```~/programs/prime-checker/main```
```
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
```

To create a unit test for this simple example, we can do the following:
<br>```python auto_test.py -i ~/programs/prime-checker/main/is-prime.py -o ~/programs/prime-checker -r 0```

The generated test might look like the following:
```
import unittest
import math

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

class TestIsPrime(unittest.TestCase):
    # Test for prime numbers
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
    
    # Test for non-prime numbers
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))

if __name__ == '__main__':
    unittest.main()
```

### Common Problems:
**TLDR:** If you want the highest level of accuracy with your generated unit tests, it is recommended that you
specify at least 1 retry attempt (```-r 1```).

A common problem with the current version of the test generator is that it will forget to write the function
you are testing in the unit test, or attempt to import the function from an invalid path. Setting ```-r``` to a value > 1
will normally catch this, but you might have to import or define the function in the generated unit test yourself. 
