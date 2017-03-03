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

    def __init__(self, parent, value) :
        """
        Input: Node (implicit argument), parent: Node, value: anything
        Output: a Node with a parent node and a value
        Purpose: constructor for a Node
        """

        self._parent = parent
        self._value = value
        if parent:
            self._depth = self._parent.depth() + 1
        else:
            self._depth = 0

        self._height = 0
        self._left = None
        self._right = None


    def updateHeights(self):
        # updating parents heights
        myTallest = self
        currNode = self._parent
        while currNode is not None:
            left = currNode.left()
            right = currNode.right()
            if left is None and right is not None:
                myTallest = right
            elif right is None and left is not None:
                myTallest = left
            else:
                if (left._height > right._height):
                    myTallest = left
                if (right._height > left._height):
                    myTallest = right
            currNode._height = myTallest._height + 1
            currNode = currNode.parent()




    def parent(self): #TODO
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the parent of this Node (if possible)
        """
        return self._parent

    def left(self):
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the left child of this node (if possible)
        """
        return self._left

    def right(self):
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the right child of this node (if possible)
        """
        return self._right

    def addLeft(self, value):
        """
        Input: Node (implicit argument), value: anything
        Output: Node (the left child)
        Purpose: add a left child to this node with the given value if there isn't one already and return it.
                If there is one already, just return the current one
        """
        if not self.hasLeft():
            self._left = Node(self, value)
            self._left._parent = self
        return self._left

    def addRight(self, value) :
        """
        Input: Node (implicit argument), value: anything
        Output: Node (the right child)
        Purpose: add a right child to this node with the given value if there isn't one already and return it.
                 If there is one already, just return the current one
        """
        if not self.hasRight():
            self._right = Node(self, value)
            self._right._parent = self
        return self._right

    def hasLeft(self):
        """
        Input: Node (implicit argument)
        Output: boolean
        Purpose: return whether this node has a left child
        """
        if self._left is not None:
            return True
        return False

    def hasRight(self):
        """
        Input: Node (implicit argument)
        Output: boolean
        Purpose: return whether the node has a right child
        """
        if self._right is not None:
            return True
        return False

    def value(self):
        """
        Input: Node (implicit argument)
        Output: anything
        Purpose: return the value stored at this Node
        """
        return self._value

    def depth(self): #TODO
        """
        Input: Node (implicit argument)
        Output: int
        Purpose: return the depth of this node in the tree in O(1)
        """

        return self._depth

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
        self._root = None
        self._right = None
        self._left = None
        self._size = 0



    def root(self):  #TODO
        """
        Input: BinTree (implicit argument)
        Output: Node
        Purpose: return the root node
        Throw a EmptyBinTreeException if the tree is empty
        """
        if self.isEmpty():
            raise EmptyBinTreeException("This tree has not yet sprouted")

        return self._root

    def parent(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: return the parent node
        Exceptions: throw an InvalidInputException if input is None
        """
        return node.parent()

    def children(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: List of child nodes
        Purpose: returns a list of direct child nodes
        Exceptions: throw an InvalidInputException if input is None
        """
        return [node.left(),node.right()]


    def isEmpty(self):
        """
        Input: BinTree (implicit argument)
        Output: boolean
        Purpose: return true if the tree is empty, false otherwise in O(1)
        """
        if self._root is None:
            return True
        return False


    def size(self):
        """
        Input: BinTree (implicit argument)
        Output: int
        Purpose: return the size of the tree in O(1)
        """
        return self._size

    def height(self):
        """
        Input: BinTree (implicit argument)
        Output: int
        Purpose: return the height of the tree in O(1) time
        Exceptions: throw an EmptyBinTreeException if the height is undefined
        """
        if self._root is None:
            raise EmptyBinTreeException("Can you climb an empty tree?")
        return self.root()._height

    def isInternal(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is internal.
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if node.hasRight() or node.hasLeft():
            return True
        return False

    def isExternal(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is external.
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if not self.isInternal(node):
            return True
        return False

    def isRoot(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is the root
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if not self._root is node:
            return False
        return True

    def left(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: get the left child of the node (if possible)
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        return node.left()


    def right(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: get the right child of the node (if possible)
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        return node.right()

    def hasLeft(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node has a left child
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if node.hasLeft():
            return True
        return False

    def hasRight(self, node): #TODO
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node has a right child
        Exceptions: throw an InvalidInputException if input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if node.hasRight():
            return True
        return False

    def addRoot(self, e): #TODO
        """
        Input: BinTree (implicit argument), e: anything
        Output: Node (the root node)
        Purpose: add a root to the tree only if there isn't one already and return it.
                 If there is one already, just return the current one
        """
        if self._root is None:
            self._root = Node(None, e)
            self._size = 1
        return self._root

    def addLeft(self, node, e): #TODO
        """
        Input: BinTree (implicit argument), node: Node, e: anything
        Output: the left child of the node
        Purpose: add a left child to the node only if there isn't one already and return it.
                 If there is one already, just return the current one
        Exceptions: throw an InvalidInputException if node input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if not self.hasLeft(node):
            left = node.addLeft(e)
            left.updateHeights()
        self._size += 1

        return node.left()


    def addRight(self, node, e): #TODO
        """
        Input: BinTree (implicit argument), node: Node, e: anything
        Output: the right child of the node
        Purpose: add a right child to the node only if there isn't one already and return it.
                 If there is one already, return it
        Exceptions: throw an InvalidInputException if node input is None
        """
        if node is None:
            raise InvalidInputException("You cannot add None")
        if not self.hasRight(node):
            right = node.addRight(e)
            right.updateHeights()
        self._size += 1

        return node.right()

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
