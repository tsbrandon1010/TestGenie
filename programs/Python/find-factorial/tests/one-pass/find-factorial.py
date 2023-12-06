
def test_factorial():
    
    # Test case for num = 0
    assert factorial(0) == 1
    
    # Test case for num = 1
    assert factorial(1) == 1
    
    # Test case for num = 5
    assert factorial(5) == 120
    
    # Test case for num = 10
    assert factorial(10) == 3628800
    
    # Test case for num = 12
    assert factorial(12) == 479001600
    
    # Test case for num = 20
    assert factorial(20) == 2432902008176640000
    
    # Test case for num = 100
    assert factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    
    # Test case for negative num, expecting a ValueError
    try:
        factorial(-1)
        assert False  # This line should not be reached
    except ValueError as e:
        assert str(e) == "Cannot find the factorial of a negative number"
    
    # Test case for large num, expecting a RecursionError (maximum recursion depth exceeded)
    try:
        factorial(100000)
        assert False  # This line should not be reached
    except RecursionError:
        assert True
