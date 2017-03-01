#! /usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import bintree

reload(bintree)
from bintree import *
import pytest


# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions.

def simple_test_1():
    # Setup simple graph
    bt = BinTree()
    bt.addRoot("A")
    bt.addLeft(bt.root(), "B")
    bt.addRight(bt.root(), "C")

    # Check graph properties using assert
    assert bt.root().value() == "A", "ERROR: Incorrect root"

    # Call this method to see what your graph looks like
    # Your program will not continue running until you exit the popup
    bt.popup()


def simple_test_2():
    # Setup slightly more complicated graph
    bt = BinTree()
    bt.addRoot(10)
    curr = bt.addLeft(bt.root(), 4)
    bt.addLeft(curr, 2)
    bt.addRight(curr, 3)
    bt.addRight(bt.root(), 8)

    assert bt.size() == 5, "ERROR: Wrong size"

    # Call this method to see what your graph looks like
    # Your program will not continue running until you exit the popup
    bt.popup()


def nodeTest():
    # create with parent and value

    # create no parent and value
    raise Exception("not implemented")


def nodeParentTest():
    # break if node doesnt have a parent
    raise Exception("not implemented")


def nodeLeftTest():
    raise Exception("not implemented")


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
    return [simple_test_1, simple_test_2]


# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__':
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
