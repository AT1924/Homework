#!/usr/bin/python
# bintree.py

""" Binary Tree module

Implement a node-and-link based Binary Tree structure

"""

from Queue import Queue
import string

class EmptyBinTreeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Node:

    def __init__(self, parent, value) : #TODO
        """
        Input: Node (implicit argument), parent: Node, value: anything
        Output: a Node with a parent node and a value
        Purpose: constructor for a Node
        """
        pass

    def parent(self): #TODO
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the parent of this Node (if possible)
        """
        return None

    def left(self): #TODO
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the left child of this node (if possible)
        """
        return None

    def right(self): #TODO
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the right child of this node (if possible)
        """
        return None

    def addLeft(self, value) : #TODO
        """
        Input: Node (implicit argument), value: anything
        Output: Node (the left child)
        Purpose: add a left child to this node with the given value if there isn't one already and return it.
                If there is one already, just return the current one
        """
        pass

    def addRight(self, value) : #TODO
        """
        Input: Node (implicit argument), value: anything
        Output: Node (the right child)
        Purpose: add a right child to this node with the given value if there isn't one already and return it.
                 If there is one already, just return the current one
        """
        pass

    def hasLeft(self): #TODO
        """
        Input: Node (implicit argument)
        Output: boolean
        Purpose: return whether this node has a left child
        """
        return False

    def hasRight(self): #TODO
        """
        Input: Node (implicit argument)
        Output: boolean
        Purpose: return whether the node has a right child
        """
        return False

    def value(self): #TODO
        """
        Input: Node (implicit argument)
        Output: anything
        Purpose: return the value stored at this Node
        """
        return None

    def depth(self): #TODO
        """
        Input: Node (implicit argument)
        Output: int
        Purpose: return the depth of this node in the tree in O(1)
        """

        return 0

    def __str__(self):
        """
        Input: Node (implicit argument)
        Output: String representation of the Node
        Purpose: printing
        """
        output = ""
        output += "(val: "
        output += repr(self.value())
        output += "; L: "
        if self.hasLeft():
            output += str(self.left())
        else:
            output += "<nothing>"
        output += "; R: "
        if self.hasRight():
            output += str(self.right())
        else:
            output += "<nothing>"
        output += ")"
        return output

class BinTree:
    """ Binary Tree class

    Implement a node-and-link based Binary Tree structure

    Author:
    Date:
    """

    def __init__(self) : #TODO
        """
        Input: BinTree (implicit argument)
        Output: BinTree
        Purpose: Creates an empty binary tree
        """
        pass

    def root(self):  #TODO
        """
        Input: BinTree (implicit argument)
        Output: Node
        Purpose: return the root node
        Throw a EmptyBinTreeException if the tree is empty
        """
        return None

    def parent(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: return the parent node
        Exceptions: throw an InvalidInputException if input is None
        """
        return None

    def children(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: List of child nodes
        Purpose: returns a list of direct child nodes
        Exceptions: throw an InvalidInputException if input is None
        """
        return None


    def isEmpty(self): #TODO
        """
        Input: BinTree (implicit argument)
        Output: boolean
        Purpose: return true if the tree is empty, false otherwise in O(1)
        """
        return False


    def size(self): #TODO
        """
        Input: BinTree (implicit argument)
        Output: int
        Purpose: return the size of the tree in O(1)
        """
        return 0

    def height(self): #TODO
        """
        Input: BinTree (implicit argument)
        Output: int
        Purpose: return the height of the tree in O(1) time
        Exceptions: throw an EmptyBinTreeException if the height is undefined
        """
        return 0

    def isInternal(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is internal.
        Exceptions: throw an InvalidInputException if input is None
        """
        return False

    def isExternal(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is external.
        Exceptions: throw an InvalidInputException if input is None
        """
        return False

    def isRoot(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is the root
        Exceptions: throw an InvalidInputException if input is None
        """
        return False

    def left(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: get the left child of the node (if possible)
        Exceptions: throw an InvalidInputException if input is None
        """
        return None

    def right(self, node):  #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: get the right child of the node (if possible)
        Exceptions: throw an InvalidInputException if input is None
        """
        return None

    def hasLeft(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node has a left child
        Exceptions: throw an InvalidInputException if input is None
        """
        return False

    def hasRight(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node has a right child
        Exceptions: throw an InvalidInputException if input is None
        """
        return False

    def addRoot(self, e): #TODO
        """
        Input: BinTree (implicit argument), e: anything
        Output: Node (the root node)
        Purpose: add a root to the tree only if there isn't one already and return it.
                 If there is one already, just return the current one
        """
        return None

    def addLeft(self, node, e): #TODO
        """
        Input: BinTree (implicit argument), node: Node, e: anything
        Output: the left child of the node
        Purpose: add a left child to the node only if there isn't one already and return it.
                 If there is one already, just return the current one
        Exceptions: throw an InvalidInputException if node input is None
        """
        return None

    def addRight(self, node, e): #TODO
        """
        Input: BinTree (implicit argument), node: Node, e: anything
        Output: the right child of the node
        Purpose: add a right child to the node only if there isn't one already and return it.
                 If there is one already, return it
        Exceptions: throw an InvalidInputException if node input is None
        """
        return None

    def __str__(self):
        """
        Input: BinTree (implicit argument)
        Output: String representation of BinTree
        Purpose: printing
        """
        toReturn = 'Size: ' + str(self.size()) + '\n'
        toReturn += 'Height: ' + str(self.height()) + '\n'
        toReturn += str(self.root())
        return toReturn


    """ Helper methods for tree visualization.
    You DON'T need to touch these """

    def graphic(self):
        """Returns a representation of this graph as a .dot file.

        In other words, if you pass the string returned by this method into
        the program DOT (or, better yet, NEATO), you can get an image file
        of the graph."""
        strs = ["graph\n{\n"]

        def annex_vertex(v):
            strs.append("\t" + str(v.value()) + ";\n")

        def annex_edge(v):
            if v.hasLeft():
                strs.append("\t" + str(v.value()) + "--" + str(v.left().value()) + ";\n")
            if v.hasRight():
                strs.append("\t" + str(v.value()) + "--" + str(v.right().value()) + ";\n")

        self.parseVerts(annex_vertex, annex_edge)
        strs.append("}\n")
        return ''.join(strs)

    def popup(self):
        """Opens a new window with this graph rendered by DOT.
        Sequential calls to this function will show the window
        once at a time. """
        import os
        tmp = open("./.tmpgraph", "w+")
        tmp.write(self.graphic())
        tmp.close()
        os.system("dot -Tpng ./.tmpgraph | display")


    def parseVerts(self, f1, f2):
        Q = Queue()
        Q.put(self.root())
        while not Q.empty():
            v = Q.get()
            f1(v)
            f2(v)
            if v.hasLeft():
                Q.put(v.left())
            if v.hasRight():
                Q.put(v.right())
