#! /usr/bin/python

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def increment(number):
    """increment: list -> list
    Purpose: Checks if input is valid and then calls increment helper.
    This should throw InvalidInputException if your list is empty or null.
    Consumes: A list of digits representing a number
    Produces: A list of 0's and 1's representing that number + 1
    """

    if number is None or []:
        raise InvalidInputException, "inputted number cannot be None or null"

    return increment_helper(number)

def increment_helper(number):
    """increment: list -> list
    Purpose: Increments a binary number by 1. This is the method that recurses on itself and actually increments the number
    Consumes: a list of 0's and 1's representing a binary number, k
    Produces: a list of 0's and 1's representing k + 1
    Example:
       increment([1,1,0,0]) -> [1,1,0,1]
    """
    # if the list is length 1 and holds only 1
    if len(number) == 1 and number[0] == 1:
        return [1,0]
    # if the last place in the list is 1
    if number[-1] == 1:
        nList = increment_helper(number[:len(number)-1])
        nList.append(0)
        return nList

    # if the last place in the list is 0
    number[-1] = 1
    return number


