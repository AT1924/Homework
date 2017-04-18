from heappriorityqueue import *
from mygraph import *

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

    return MyGraph()

class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
