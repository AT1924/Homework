#!/usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import hashset
reload(hashset)
from hashset import *
import pytest

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions. Feel free to delete example_test_1
# and remove it from the list in get_tests().

def example_test_1():
    assert 1 == 1, 'Error: 1 does not equal 1!'

def simple_test():
   # Set up hashset
   hashy = HashSet()

   # Make sure set is initially empty
   assert hashy.is_empty() == True

   # Insert 5 different elements
   hashy.insert('ACT')
   hashy.insert('BYE')
   hashy.insert('CAT')
   hashy.insert('DOG')
   hashy.insert('EGG')

   # Make sure set is no longer empty
   assert hashy.is_empty() == False

   # Remove each of the added elements
   hashy.remove('ACT')
   hashy.remove('BYE')
   hashy.remove('CAT')
   hashy.remove('DOG')
   hashy.remove('EGG')

   # Make sure set is empty once again
   assert hashy.is_empty() == True

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
    return [example_test_1, simple_test]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
