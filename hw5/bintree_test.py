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
    # create with no parent and value
    par = Node(None,"A")
    assert par.value() == "A", "The value of the node is not correct"

    # create parent and value
    bNode = Node(par,"B")
    assert bNode.parent() is par, "The parent of nodeTest is not defined"


def nodeTest2():

    # break if node does have a parent
    rt = Node(None, None)
    assert rt.parent() is None

    assert rt.value() is None

    assert rt.depth() is 0

    assert rt._height is 0

    assert rt.left() is None

    assert not rt.right() and not rt.left()

def nodeChildTest():
    rt = Node(None, "A")

    assert not rt.hasLeft() and not rt.hasRight()

    left = rt.addLeft("B")
    right = rt.addRight("C")

    assert left.value() is "B"
    assert rt.left() is left

    assert right.value() is "C"
    assert rt.right() is right

    assert left.depth() is 1
    assert right.depth() is 1

    assert rt.hasLeft() and rt.hasRight()

def binTreeTest():
    # test empty tree
    bt = BinTree()
    assert bt.isEmpty()
    assert bt.size() is 0
    assert bt.root() is None

    # test adding a root node
    root = bt.addRoot("A")
    assert root is bt.root()
    assert bt.isRoot(root)

    # test having and not having children
    assert bt.left(root) is None
    assert bt.right(root) is None

    right = bt.addRight(root,"B")
    left = bt.addLeft(root,"C")
    assert bt.hasLeft(root)
    assert bt.hasRight(root)
    assert bt.right(root) is right
    assert bt.left(root) is left

def binTreeInternal_External():
    bt = BinTree()
    root = bt.addRoot("A")

    assert bt.isExternal(root)
    left = bt.addLeft(root, "B")
    assert bt.isExternal(left)
    right = bt.addRight(root, "C")
    leftGrandChild = bt.addLeft(left, "D")

    assert bt.isInternal(root)
    assert bt.isInternal(left)
    assert bt.isExternal(right)
    assert bt.isExternal(leftGrandChild)

def binTreeHeight_Depth():
    bt = BinTree()
    root = bt.addRoot("A")
    left = bt.addLeft(root, "B")
    right = bt.addRight(root, "C")
    leftGrandChild = bt.addLeft(left, "D")

    assert bt.height() == 2

def binTreeParent_Child():
    bt = BinTree()
    root = bt.addRoot("A")
    left = bt.addLeft(root, "B")
    right = bt.addRight(root, "C")
    leftGrandChild = bt.addLeft(left, "D")

    assert root is  bt.parent(left) and root is bt.parent(right)
    assert leftGrandChild in bt.children(left)

    assert not bt.isEmpty()
    assert bt.size() == 4


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
    return [simple_test_1, simple_test_2, nodeTest, nodeTest2, nodeChildTest, binTreeTest, binTreeInternal_External, binTreeHeight_Depth, binTreeParent_Child]


# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__':
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
