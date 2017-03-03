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


def test_Innit():
    # trigger exceptions
    with pytest.raises(InvalidInputException):
        HashSet(expected_size=250)
        HashSet(key_length=2)

    # create hash set
    hashy = HashSet(expected_size=300, key_length=5)

    # check if it has an array of random numbers for letter in alphabet
    assert (len(hashy._keyRandoms) == 5)
    assert (hashy._expected_size == 300)


def test_Insert():
    # test exceptions: key null, key is incorrect length
    hashy = HashSet()

    with pytest.raises(InvalidInputException):
        hashy.insert(None)
        hashy.insert('ABCD')

    # add something that is not in the hash set: make sure length is correct
    hashy.insert('ABC')
    assert hashy.size() == 1, "The length of the hashset is the number of hashes, in this case 1"

    # add something in the hash set: make sure length does not change
    hashy.insert('ABC')
    assert hashy.size() == 1, "The length of the hashset is the number of hashes, in this case 1"


def test_Contains():
    # do for an empty hashset and a hashset with values in it
    hashy = HashSet()
    hashy.insert('ABC')
    # test to see if key is not contained
    assert not hashy.contains('ABC') == False, "The hash set does contain key"

    # test to see if key is contained
    assert hashy.contains('ABC') == True, "Contains is True, thus the key is contained"


def test_Remove():
    # do for empty hashset and hashset with values in it


    # For empty hash set
    hashy = HashSet()
    # if key isnt in hashset
    assert hashy.remove('ABC') == None, "This key is not in the hash set"

    # if key is in hashset
    hashy.insert("ABC")
    assert hashy.remove("ABC") == "ABC", "The key has not been successfully removed"

    # for hash set with values
    hashy.insert("XYZ")
    hashy.insert("DEF")
    hashy.insert("GHI")
    # if key isnt in hashset
    assert hashy.remove("LMN") == None, "This key is not in the hash set"

    # if key is in hashset
    assert hashy.remove("XYZ") == "XYZ", "This key has not been successfully removed"


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
    return [example_test_1, simple_test, test_Innit, test_Insert, test_Contains, test_Remove]


# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__':
    print 'Running tests...'
    tests = get_tests()
    for test in get_tests():
        test()
    print 'All tests passed!'
