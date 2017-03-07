#! /usr/bin/python

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


""" Preorder, Inorder, Postorder, and Breadth First Traversals of a Binary Tree

"""

def preorder(bt):
    """preorder: binary tree -> list[Position]
    Purpose: Runs a preoder traveral on the binary tree.
    Consumes: a binary tree
    Produces: a list of Position objects preorder
    Example:       A
       preorder(  / \  ) -> [A B C]
                 B   C
    If tree is empty, should return an empty list. If the tree
    is null, you should throw InvalidInputException.
    """
    return []

def inorder(bt):
    """inorder: binary tree -> list[Position]
    Purpose: Runs a preoder traveral on the binary tree
    Consumes: a binary tree
    Produces: a list of Position objects inorder
    Example:       A
        inorder(  / \  ) -> [B A C]
                 B   C
    If tree is empty, should return an empty list. If the tree
    is null, you should throw InvalidInputException.
    """
    return []

def postorder(bt):
    """postorder: binary tree -> list[Position]
    Purpose: Runs a preoder traveral on the binary tree
    Consumes: a binary tree
    Produces: a list of Position objects postorder
    Example:       A
      postorder(  / \  ) -> [B C A]
                 B   C
    If tree is empty, should return an empty list. If the tree
    is null, you should throw InvalidInputException.
    """
    return []

def breadthfirst(bt):
    """breadthfirst: binary tree -> list[Node]
    Purpose: Runs a breadth first search on a binary tree
    Consumes: a binary tree object
    Produces: a list of Nodes in breadth first search order
    Example:
                    A
    breadthfirst(  / \  ) -> [A B C]
                  B   C
    If tree is empty, should return an empty list. If the tree
    is null, you should throw InvalidInputException.
    """
    return []
