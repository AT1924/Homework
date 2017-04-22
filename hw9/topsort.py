""" Topological Sort

"""
from collections import deque
from mydigraph import *



def topological_sort(dag):
    """topological_sort: dag -> list of vertices
    Purpose: Runs a topological sort on a DAG
    Consumes: a directed acyclic graph
    Produces: a list of topologically sorted vertices, or empty list if graph is empty
    Raises: A GraphCycleException if no topological sorting
        is possible on the input DAG
	An InvalidInputException if the graph is None.
    Example:                    A -\
             topological_sort(      C -> D ) -> [A, B, C, D]
                                B -/
    """
    # return invalid input
    if dag is None:
        return InvalidInputException("dag is none")

    # initialize stack and list
    vertexStack = []
    sortList = []
    vertices = dag.vertices()


    # first check for cycle in graph


    # loop thru to find if vertex is a source
    for vertex in vertices:
        # append to stack if vertex is a source
        if dag.incidentEdges(vertex) == 0:
            vertexStack.append(vertex)
    while len(vertexStack) is not 0:
        vertex = vertexStack.pop()
        sortList.append(vertex)
        edges = dag.eminentEdges(vertex)
        for edge in edges:
            w = findEndVertex(dag, edge)
            dag.removeEdge(edge)
            if dag.incidentEdges(w) == 0:
                vertexStack.append(w)

    return sortList

def findEndVertex(dag, edge):
    toAndFrom = dag.endVertices(edge)
    if len(toAndFrom) == 2:
     return toAndFrom[1]



class GraphCycleException(Exception):
    def __str__(self):
        return "Topological sort failed. A cycle occured."


class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
