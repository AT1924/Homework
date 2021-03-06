from mygraph import *


def shortest_path(g, v_start, v_to_find):
    """Input: Graph, GraphVertex, GraphVertex -> [GraphVertex]
    Purpose: Determine the shortest path in the graph from v_start v_to_find.
    The method should return a list consisting of the shortest path from
    v_start to v_to_find. The first element of the returned list should
    be v_start and the last should be v_to_find. If there is no path
    between the start and end vertices, return an empty list.
    Example: path.shortest_path(g, v_start, v_to_find) -> [v_start, v1, v2, v_to_find]
    Throws: InvalidInputException if any input is None or either vertex
    is not in g.
    """
    shortestPath = []
    found = False
    queue = []
    decorate = {}

    # add start node to queue
    queue.append(v_start)
    # iterate on queue and decorate neighbors that have not been decorated
    while len(queue) != 0 and not found:
        vertex = queue.pop(0)
        # get to last node, and trace back to first node
        if vertex is v_to_find:
            found = True
            while vertex is not v_start:
                shortestPath.insert(0, vertex)
                vertex = decorate[vertex]
            shortestPath.insert(0, v_start)

        for edge in g.incidentEdges(vertex):
            nextVertex = g.opposite(vertex, edge)
            if nextVertex not in decorate:
                decorate[nextVertex] = vertex
                queue.append(nextVertex)

    # or else return empty list
    return shortestPath
