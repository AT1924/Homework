#!/usr/bin/python

# DO NOT DELETE THESE STATEMENTS
import queue
reload(queue)
from queue import *
import pytest

# Write your testing functions here! Each testing function should have an
# informative name and test a specific aspect of your program's functionality.
# It is fine to have multiple assert statements in each function to test for
# various related conditions.

# Here are some example test functions.

def test_1() :
    """This enqueues a number, then dequeues it.
    """
    q = Queue(4)
    assert q.is_empty() == True, "Test 1 failed: Should return true"
    q.enqueue(3)
    assert q.dequeue() == 3, "Test 2 failed: Should return 3"

def test_input_error():
    """This is an example input error checking.
    """
    q = Queue(5)
    with pytest.raises(EmptyQueueException):
        q.dequeue()


def test_listAtFullCapacity():
    q = Queue(1)
    q.enqueue(1)
    assert q.capacity() == 2, "Incorrect Capacity"
    assert q.dequeue() == 1

def testWrappedQueue():
    # test enqueueing and dequeueing item on wrapped list
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4

def testShrinkCapacity():
    q = Queue(4)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    assert q.capacity() == 2

def testQueue():
    q = Queue(4)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

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
    return [test_1, test_input_error, test_listAtFullCapacity, testWrappedQueue, testQueue, testShrinkCapacity]

# DO NOT EDIT BELOW THIS LINE ==================================================

# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
