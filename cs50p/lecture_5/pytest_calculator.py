from calculate import square

"""
def test_square():
    assert square(3) == 9
    assert square(0) == 0
    assert square("cat") == 8 #? type error
    assert square(2) == 3 #? assertion error
    assert square(4) == 16
    assert square(5) == 25
"""

"""
This module contains unit tests for the `square` function from the `calculate` module.
The below tests are divided into three categories:
1. `test_positive`: Tests the `square` function with positive integers.
2. `test_negative`: Tests the `square` function with negative integers.
3. `test_zero`: Tests the `square` function with zero.
The commented-out `test_square` function includes additional test cases, such as testing with a string input and an incorrect assertion, which are not currently active.
Note:
- The `test_negative` function contains an incorrect assertion for `square(-4)`, which is expected to fail.
- The `test_zero` function contains an incorrect assertion for `square(0)`, which is expected to fail.
These tests are designed to verify the correctness of the `square` function and to identify any potential issues or edge cases.

"""
 
def test_positive():
    assert square(3) == 9
    assert square(0) == 0
    assert square(4) == 16
    assert square(5) == 25

def test_negative():
    assert square(-3) == 9
    assert square(-4) == 3
    assert square(-5) == 25

def test_zero():
    assert square(0) == 10

