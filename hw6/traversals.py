#! /usr/bin/python

import bintree
reload(bintree)
from bintree import *

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
    if bt is None:
        raise InvalidInputException("empty trees can only grow empty fruits")

    if bt.isEmpty():
        return []

    nodes = []
    root = bt.root()
    nodes.append(root)

    if root.hasLeft():
        leftTree = bintree.BinTree()
        leftTree.addRoot(root.left())
        nodes.extend(preorder(leftTree))

    if root.hasRight():
        rightTree = bintree.BinTree()
        rightTree.addRoot(root.right())
        nodes.extend(preorder(rightTree))

    return nodes

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


    if bt is None:
        raise InvalidInputException("empty trees can only grow empty fruits")

    if bt.isEmpty():
        return []

    nodes = []
    root = bt.root()

    if root.hasLeft():
        leftTree = bintree.BinTree()
        leftTree.addRoot(root.left())
        nodes.append(inorder(leftTree))

    nodes.append(root)

    if root.hasRight():
        rightTree = bintree.BinTree()
        rightTree.addRoot(root.right())
        nodes.append(inorder(rightTree))




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
    if bt is None:
        raise InvalidInputException("empty trees can only grow empty fruits")

    if bt.isEmpty():
        return []

    nodes = []
    root = bt.root()


    if root.hasLeft():
        leftTree = bintree.BinTree()
        leftTree.addRoot(root.left)

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
    if bt.isEmpty():
        raise InvalidInputException("empty trees can only grow empty fruits")

    return []
