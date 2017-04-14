#!/usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import sort
reload(sort)
from sort import *
import pytest

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions. Feel free to delete example_test_1
# and remove it from the list in get_tests(), and feel free to add to simple_test.

def example_test_1():
    assert 1 == 1, 'Error: 1 does not equal 1!'

def simple_test():
    # This loops through all of your sort algorithms, and
    # runs any asserts in the for loop on each one.
    sort_algorithms = [(merge_sort, "Merge sort"), (quick_sort, "Quick sort"), (radix_sort, "Radix sort")]
    for sort_algorithm, name in sort_algorithms:
        assert sort_algorithm([4,5,1,3,2]) == [5,4,3,2,1], "%s failed." % name
	    # Add many, many more asserts here to test your sorts!

def merge_sort_test():
    array = [3,5,1,2,10,9,5]
    assert merge_sort(array) == [10,9,5,5,3,2,1]

    with pytest.raises(InvalidInputException):
        merge_sort(None)

def quick_sort_test():
    array = [10,5,7,20,8,3]
    assert quick_sort(array) == [20,10,8,7,5,3]

    with pytest.raises(InvalidInputException):
        quick_sort(None)

def get_tests():
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # VERY IMPORTANT
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

    # return [example_test_1, simple_test, merge_sort_Test()]
    return [example_test_1, merge_sort_test, quick_sort_test]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
