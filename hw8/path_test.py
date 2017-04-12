#!/usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import path
import mygraph
reload(mygraph)
reload(path)
from mygraph import *
from path import *
import pytest

def format_list(l):
    # Returns a list of GraphVertex objects in string format.

    if l != None:
        return "[" + ", ".join([str(v) for v in l]) + "]"
    else:
        return ""

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions. Feel free to delete example_test_1
# and remove it from the list in get_tests().

def example_test_1():
    assert 1 == 1, 'Error: 1 does not equal 1!'

def simple_test():
    # Setup simple graph
    g = MyGraph()
    v0 = GraphVertex(0)
    v1 = GraphVertex(1)
    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertEdge(v0, v1, GraphEdge(0))

    # Run the algorithm
    path = shortest_path(g, v0, v1)
    print "Shortest path found: " + format_list(path)

    # Throw an exception so we know our test failed
    assert path == [v0, v1]

    # Call this method to see what your graph looks like
    # Your program will not continue running until you exit the popup
    g.popup()

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
    return [example_test_1, simple_test]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
