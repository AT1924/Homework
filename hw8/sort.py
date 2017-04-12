#!/usr/bin/python

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        

def merge_sort(array):
    """merge_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the merge sort algorithm
        Example: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    return array


def quick_sort(array):
    """quick_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the quicksort algorithm
        Example: quick_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    return array


def radix_sort(array):
    """radix_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the radixsort algorithm
        Example: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    return array
