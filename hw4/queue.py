#!/usr/bin/python
# Queue.py

""" Queue Class
Implement a growable and shrinkable queue with an array as
the underlying data structure

IMPORTANT: Do not use the python's built-in Queue functionality.
Python has Queue functionality built into its lists. You will
receive no credit for using any built in Queue functionality.
"""

import string


class Queue:

    def __init__(self, initial_capacity):
        """init: queue * num -> .
        purpose: initialize queue
        consumes: a queue and a number
        Produces: nothing
        Raises: InvalidInputException:  initial_capacity negative or null
        Example: Queue(9) -> An Empty Queue with space for 9 elements
        """
        # cannot create negative 0 or negative capacity
        if initial_capacity < 1:
            raise InvalidInputException("initial capacity must be at least 1")
        self.myCapacity = initial_capacity
        self._myList = [None] * initial_capacity
        self.end, self.begin = 0, 0
        self.mySize = 0


    def size(self):
        """size: queue -> num
        purpose: returns number of items currently in queue
        consumes: a queue
        Produces: the number of items in the queue
        Example: size() -> 9
        """
        return self.mySize

    def is_empty(self):
        """is_empty: queue -> bool
        purpose: tell whether the queue is empty or not
        consumes: a queue
        Produces: boolean
        Example: is_empty() -> false
        """
        return self.mySize == 0

    def enqueue(self,any):
        """enqueue: queue * any -> .
        purpose: add an arbitrary type to the end of the queue
        consumes: a queue and an arbitrary type
        Produces: nothing
        Example: enqueue("sarah") -> the string sarah is added to the end of the queue
        """
        # enqueue item
        self._myList[self.end] = any
        self.end += 1
        self.mySize += 1

        # if we have reached capacity increase list size
        if self.size() == self.capacity():
            newList = [None] * 2 * self.capacity()

            index = self.begin
            for i in range(self.size()):
                newList[i] = self._myList[index]
                index += 1
                if index == self.capacity():
                    index = 0
            self.begin = 0
            self.end = self.size()

            self._myList = newList
            self.myCapacity = self.capacity() * 2

        #wrapped
        if self.end == self.capacity():
            self.end = 0

    def dequeue(self):
        """dequeue: queue -> any
        purpose: removes and returns first item in queue
        (throws EmptyQueueException if empty)
        consumes: a queue
        Produces: first element in the queue
        Raises: EmptyQueueException: trying to dequeue from empty queue
        Example: dequeue() -> "sarah"
        """
        # if queue is empty
        if self.is_empty():
            raise EmptyQueueException("I don't feel like it")

        # get begin value
        val = self._myList[self.begin]
        self._myList[self.begin] = None
        self.begin += 1
        self.mySize -= 1

        # wrapped
        if self.begin >= self.capacity():
            self.begin = 0

        # shrink when size is less than one quarter and capacity is greater than 3
        if self.size() <= self.capacity()/ 4 and self.capacity() > 3:
            newList = [None] * (self.capacity()/2)
            index = self.begin
            for i in range(self.size()):
                newList[i] = self._myList[index]
                index += 1
            self._myList = newList
            #update capacity
            self.myCapacity = self.capacity() / 2
            self.begin = 0
            self.end = self.size()

        return val



    def front(self):
        """front: queue ->  any
        purpose: returns first item in queue without removing it (throws empty queue exception if empty)
        consumes: a queue
        Produces: the first item in the queue
        Raises: EmptyQueueException: trying to find element from empty queue
        Example: front() -> "sarah"
        """
        if self.is_empty():
            raise EmptyQueueException("Only when we are empty can we begin again")
        return self._myList[self.begin]

    def capacity(self):
        """capacity: queue -> num
        purpose: returns how many elements the queue can hold
        consumes: a queue
        Produces: number of elements the queue can hold
        Example: capacity() -> 16
        """
        return self.myCapacity



class EmptyQueueException(Exception):
    """EmptyQueueException: Exception -> stack trace
    purpose: produce stack trace when an error is encountered due to an empty queue
    consumes: an exception
    Produces: stack trace
    Example: raise EmptyQueueException
    """
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidInputException(Exception):
    """InvalidInputException: Exception -> stack trace
    purpose: produce stack trace when an error is encountered due to an invalid input
    consumes: an exception
    produces: stack trace
    Example: raise InvalidInputException
    """
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
