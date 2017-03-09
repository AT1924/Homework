#! /usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import bintree
import traversals
reload(bintree)
reload(traversals)
from bintree import *
from traversals import *
import pytest

def show_values(l):
    """
    This function takes in a list of nodes and produces a list of just the nodes' values.
    The purpose of this function is to make the output of your traversals more readable.
    You are not required to use this function, but it might be helpful!
    """
    if l != None:
        return [x.value() for x in l]
    else:
        return []

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions. Feel free to delete example_test_1
# and remove it from the list in get_tests().

def example_test_1():
    assert 1 == 1, 'Error: 1 does not equal 1!'

def simple_test():
    # Setup the tree
    bt = bintree.BinTree()
    root = bt.addRoot("Root")
    left = bt.addLeft(root, "Left")
    right = bt.addRight(root, "Right")

    # Run the algorithm
    pre = preorder(bt)

    # Test its output
    print "Preorder is in this order: " + str(show_values(pre))
    assert pre == [root, left, right], "Preorder missed assertion!"

def preorder_Test():
    with pytest.raises(InvalidInputException):
        preorder(None)

    bt = bintree.BinTree()
    assert preorder(bt) == []
    root = bt.addRoot("A")
    left = bt.addLeft(root, "B" )
    leftLeftGrandChild = bt.addLeft(left, "D")
    leftRightGrandChild = bt.addRight(left, "E")
    right = bt.addRight(root, "C")
    rightLeftGrandChild = bt.addLeft(right, "F")
    rightRightGrandChild = bt.addRight(right, "G")

    nodes = preorder(bt)

    assert nodes == [root, left, leftLeftGrandChild, leftRightGrandChild, right, rightLeftGrandChild, rightRightGrandChild]

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
    return [example_test_1, simple_test, preorder_Test]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
