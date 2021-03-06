#!/usr/bin/python
import random

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
    if array is None:
        raise InvalidInputException('Null array')

    if len(array) < 2:
        return array
    L = []
    E = []
    G = []
    pivot = array[random.randrange(0, len(array))]
    for element in array:
        if element < pivot:
            L.append(element)
        elif element > pivot:
            G.append(element)
        else:
            E.append(element)
    return quick_sort(G) + E + quick_sort(L)


def radix_sort(array):
    """radix_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the radixsort algorithm
        Example: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """

    if array is None:
        raise InvalidInputException('Null array')

    # list with 10 buckets 0-9

    posBuckets = [[] for _ in range(10)]
    negBuckets = [[] for _ in range(10)]

    # loop "num_digits" times
    counter = 1
    num_digits = len(str(max(array)))

    while counter <= num_digits:

        # loop on array
        while len(array) > 0:
            # check current digit in array and place it into corresponding bucket
            num = array.pop()
            numAsString = str(num)
            if num < 0:
                buckets = negBuckets
            else:
                buckets = posBuckets
            if len(numAsString) < counter or numAsString[-counter] == "-":
                buckets[0].append(int(numAsString))
            else:
                buckets[int(numAsString[-counter])].append(int(numAsString))

        # outside of loop, concatenate the buckets
        # positive
        while len(posBuckets) > 0:
            bucket = posBuckets.pop()
            while len(bucket) > 0:
                array.append(bucket.pop())
        posBuckets = [[] for _ in range(10)]

        # negative
        while len(negBuckets) > 0:
            bucket = negBuckets.pop(0)
            while len(bucket) > 0:
                array.append(bucket.pop(0))
        negBuckets = [[] for _ in range(10)]

        counter += 1

    return array
