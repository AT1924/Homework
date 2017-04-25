from heappriorityqueue import *
from mygraph import *
from math import *


def dijkstra(g, src):
    """ Calculate the shortest path tree from the src in the input
    connected graph using Dijkstra's algorithm. The elements attached
    to the edges should be the distances. Must run in O((|E| + |V|) log |V|)
    time using the provided HeapPriorityQueue data structure.

    Returns the shortest path tree in the form of a new MyGraph object.
    Do not modify the input MyGraph instance.

    Raise the InvalidInputException if input is None or if src is not in g.

    Note: To access the actual vertices in the HeapPriorityQueue,
    you need to call pop().value(), not just pop().
    """
    # raise exception if input is None or src is not in g
    if g is None or g.containsVertex(src) is False:
        raise InvalidInputException("g is none or g does not contain src")

    #solution:
    shortestPath = MyGraph()

    #add all vertices from g into heap priority queue

    #take source, get children, add children, repeat for each child
    hQueue = HeapPriorityQueue()

    vertex = src
    hQueue.push(vertex, )





















    # loop thru all vertices and initialize distance decorations, infinity for all but src
    elements = []
    heapPos = {}
    decorate = {}
    vertices = g.vertices()
    for vertex in vertices:
        #vertex.element = float('inf')
        vertex.element = float("inf")
        elements.insert(0, vertex.element)
        decorate[vertex] = None

    # set distance of src to 0
    src.element = 0
    elements.insert(0, src)

    # initalize PQ and use vertex.elements as priorities
    pQueue = HeapPriorityQueue()

    #TODO -- fix adding to HeapPriorityQueue
    for vertex in vertices:
        position = pQueue.push(vertex.element, vertex).pos()
        heapPos[vertex.element] = position

    # while it is not empty ect..
    while len(pQueue):
        popped = pQueue.pop()
        vertex = popped.value()
        print vertex.element()
        print type(vertex)
        g.removeVertex(vertex)
        decorate[vertex] = 1
        edges = g.incidentEdges(vertex)
        for edge in edges:
            nextVertex = g.opposite(vertex, edge)
            dist = vertex.element + g.connectingEdge(vertex, nextVertex).element()
            if dist < nextVertex.element:
                e = pQueue.Entry(nextVertex.element, nextVertex, heapPos[nextVertex.element])
                nextVertex.element = dist
                decorate[nextVertex] = vertex
                # why is this not in the heap
                pQueue.replaceKey(e, nextVertex.element)
                # for all edges, decorate according to cost
                # for edge in g.incidentEdges(vertex):
                #  nextVertex = g.opposite(vertex, edge)

                # if nextVertex.element > vertex.element + edge.element():
                #   nextVertex.element = vertex.element + edge.element()

                # set prev marker and replace in PQ
                shortestPath.insert(0, vertex)
                #decorate[nextVertex] = vertex

    # return myGraph object of the shortestPath
    path = MyGraph()
    for vertex in shortestPath:
        next = shortestPath[vertex + 1]
        path.insertVertex(vertex)
        path.insertEdge(vertex, next, g.connectingEdge(vertex, next))



        # return shortest path tree in the form of a new MyGraph object, what does this mean?
        # basically want to create a graph that
    return path


def getPosOfEntryInPQ(pq):
    return pq.entry.pos()


def initalizeQueue(key, value, pos):
    pQueue = HeapPriorityQueue


class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
