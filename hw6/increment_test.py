#!/usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import increment
reload(increment)
from increment import *
import pytest

def strToList(string):
    """
    This function takes in a string of numbers (example: '111') and turns
    it into a list of integers. The purpose of this function is to make
    it easier to call increment. For example, instead of calling
        increment([1,1,1])
    you could write
        increment(strToList('111'))
    You are not required to use this function, but it might be helpful!
    """
    return [int(x) for x in string]

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions. Feel free to delete them and remove them
# from the list in get_tests.

def example_test_1():
    assert 1 == 1, 'Error: 1 does not equal 1!'

def example_test_2():
    my_list = []
    assert len(my_list) == 0, 'Error: The list is not empty...'

def helperTest():

    with pytest.raises(InvalidInputException):
        increment(None)
        increment([])

    assert increment(strToList("0")) == [1]
    assert increment(strToList("1")) == [1,0]
    assert increment(strToList("10")) == [1,1]
    assert increment(strToList("11")) == [1,0,0]
    assert increment(strToList("100")) == [1,0,1]
    assert increment(strToList("101")) == [1,1,0]



def get_tests():
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # IMPORTANT
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Add the names of each of your test functions to this list. It is very
    # important that you do this, or the TAs will not run your tests properly
    # and you will not receive full credit.
    #
    # DO NOT remove either example test from this list, just add new tests like so:
    #       [example, example, new test,...]
    # We will not be able to properly grade your coal tests if you do not follow
    # these instructions! You will lose points on your submission for failing
    # to follow these instructions.
    return [example_test_1, example_test_2, helperTest]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
