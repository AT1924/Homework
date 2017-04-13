#!/usr/bin/python

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
def merge(a,b):
    result = []
    total = len(a) + len(b)
    while len(result) < total:
        if len(a) > 0 and len(b) > 0:
            #append larger element to result
            if a[0] > b[0]:
                result.append(a.pop(0))
            else:
                result.append(b.pop(0))
        elif len(a) > 0:
            result.extend(a)
        else:
            result.extend(b)
    return result


def merge_sort(array):
    """merge_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the merge sort algorithm
        Example: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    if array is None:
        raise InvalidInputException('Null array')

    # if length is < 2 return array
    if len(array) < 2:
        return array

    # select midpoint, n/2  blank:len/2, len/2:
    # run mergesort on left and right components
    # return the merging of the left and right components
    return merge(merge_sort(array[:len(array)/2]), merge_sort(array[len(array)/2:]))



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
