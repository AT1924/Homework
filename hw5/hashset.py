#! /usr/bin/python
# hashset.py

""" HashSet module

Implement a HashSet with an array/list as the underlying data structure

IMPORTANT: Do not use the python's built-in hash set functionality. 
Python has built in sets and dictionaries that work better than the hash set
you are going to implement. You will receive no credit if you use Python's sets 
or dictionaries. You should only need to use Python lists.
"""
import string
import sys
import os
import random

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def smallest_prime(start):
    """
    Input: The starting number
    Output: The smallest prime >= start
    Purpose: Finds the smallest prime >= start and returns it.
    """
    while not is_prime(start):
        start += 1
    return start

def is_prime(num):
    """
    Input: num - The number to check for primality
    Output: True if num is prime, False otherwise.
    Purpose: Check if num is prime.
    """
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


class HashSet:
    """ HashSet Class
    Implement a hash set with an array/list as the underlying data structure
    """

    def __init__(self, expected_size=256, key_length=3):
        """
        Input:  self - hash set object
                expected_size - the size of the hash set, default is 256.
                      Note that even if expected_size is composite, the size of 
                      the underlying data-structure should be prime.
                key_length - the length of keys for this hash set, default is 3.
        Output: Nothing
        Purpose: Create HashSet and initialize member variables. Should be 
                 O(smallest prime greater than expected_size).
        Exceptions: Raise InvalidInputException if either input is None or less 
                    than 1.
        """

        # TODO Check for invalid inputs!

        if key_length < 3 or expected_size < 256:
            raise InvalidInputException("key length must be >= 3 or expected size must be at least 256")


        # Initialized variables based on parameters.
        self._expected_size = expected_size
        self._key_length = key_length

        # Find smallest prime greater than expected_size, or 256. 
        if expected_size <= 256:
            self.prime = smallest_prime(256)
        else:
            self.prime = smallest_prime(expected_size)

        # Underlying array for hashset.
        self._hashset = [[] for i in range(self.prime)]
        self._hashset_size = 0

        # generate random keys
        self._keyRandoms = []
        for i in range (key_length):
            self._keyRandoms.append(random.randint(0,expected_size-1))


    def my_hash(self, key):
        """
        Input: key - key to hash
        Output: The hash of the key 
        Purpose: Generates a hash value for the given key by computing:
                 (a1*x1 + ... + ak*xk) % p where:
                 x1..xk are the numeric values of the n characters in the key
                 
                 a1..ak are random numbers picked during initialization of the 
                 hash set
                 NOTE: a1...ak are picked during initialization so that all calls
                       to Hash use the same a1...ak (but they are randomly 
                       generated for each HashSet)
                 
                 p is the smallest prime number greater than or equal to the 
                 capacity of the set (which must be at least 256). This will 
                 compute an integer which will then be used as the index in to 
                 the array.
        Exceptions: throw an InvalidInputException if the input key is None or 
                    the wrong length.     
        """

        if key is None or len(key) != self._key_length:
            raise InvalidInputException("key must not be none and equal to key length")



        sum = 0
        for i in range (self._key_length):
          sum += self._keyRandoms[i]  *  ord(key[i])
        return sum % self.prime


    def insert(self, key):
        """
        Input: key - the key to insert into the set
        Output: Nothing
        Purpose:
            Add an element to the hashset in O(1) expected time.

            If there is a miss, insert key at the hash-key index.
            If there is a hit with the same key, ignore it. 
            If there is a hit with a different key, add the new entry to the same
            bucket.
        Exceptions: throw an InvalidInputException if the input key is None or 
                    the wrong length.
        """

        if key is None or len(key) != self._key_length:
            raise InvalidInputException("key must not be none and equal to key length")


        if self.contains(key):
            pass
        else:
            index = self.my_hash(key)
            bucket = self._hashset[index]
            if key not in bucket:
                bucket.append(key)
                self._hashset_size += 1


    
    def contains(self, key):
        """
        Input: key - hash key
        Output: True if the key is present, False otherwise.
        Purpose: Check if a key is present in the set in O(1) expected time.
        Exceptions: throw an InvalidInputException if the input key is None or 
        the wrong length.
        """

        index = self.my_hash(key)
        bucket = self._hashset[index]
        if key in bucket:
            return True

        return False
    
    def remove(self, key):
        """
        Input: key - hash key
        Output: The key if it is present in the set, and None otherwise.
        Purpose: Find the key in the set (if present), remove it, and return it.
        Return None otherwise. Expected O(1) time.
        Exceptions: throw an InvalidInputException if the input key is None or 
        the wrong length.
        """

        if key is None or len(key) != self._key_length:
            raise InvalidInputException("key must not be none and equal to key length")

        if self.contains(key):
            index = self.my_hash(key)
            bucket = self._hashset[index]
            self._hashset_size -= 1
            return bucket.pop(bucket.index(key))
        else:
            return None


    
    def get_keys(self):
        """
        Input: Nothing
        Output: A list of all keys in the set
        Purpose: Return a list of all the keys in the set. Runtime should be 
        O(m*n) worst case, where m is the number of buckets and n is the number 
        of elements in each bucket. 
        """

        key_list = []
        for bucket in self._hashset:
            for key in bucket:
                key_list.append(key)

        return key_list

    def size(self):
        """
        Input: Nothing
        Output: The number of items in the set
        Purpose: Return the number of items in the hash set.
        """

        return self._hashset_size

    def is_empty(self):
        """
        Input: Nothing
        Output: True if the set is empty, False otherwise.
        Purpose: Return if the set is empty.
        """

        return self._hashset_size == 0
        
    def clear(self):
        """
        Input: Nothing
        Output: Nothing
        Purpose: Remove all keys from the hash set.
        """
        self._hashset = [[] for i in range(self._prime)]
        self._hashset_size = 0
        
    def __str__(self):
        """
        Input: Nothing
        Output: A string representation of the set
        Purpose: This gets called when the class gets converted to a string. It
        is useful for debugging.
            
        >>> a = HashSet()
        >>> print a
        """
        toReturn = '{'
        for k in self.get_keys():
            toReturn += k + ', '
        toReturn = toReturn.rstrip(', ') + "}"    
        return toReturn
