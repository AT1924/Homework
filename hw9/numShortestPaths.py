class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."


def numShortestPaths(g, start, end):
    """graph, start node, end node -> int
    Purpose: find the number of shortest paths between two nodes in a graph
    Raises: raise InvalidInputException if an input is None, or 
    if start or end are not in g"""
    shortestPath = []
    found = False
    queue = []
    decorate = {}

    # add start node to queue
    queue.append(start)
    # iterate on queue and decorate neighbors that have not been decorated
    while len(queue) != 0 and not found:
        vertex = queue.pop(0)
        # get to last node, and trace back to first node
        if vertex is end:
            found = True
            #count paths
            while vertex is not start:
                shortestPath.insert(0, vertex)
                vertex = decorate[vertex]
            shortestPath.insert(0, start)

        for edge in g.incidentEdges(vertex):
            nextVertex = g.opposite(vertex, edge)
            if nextVertex not in decorate:
                decorate[nextVertex] = [vertex]
                queue.append(nextVertex)
            else:
                decorate[nextVertex].append(vertex)

                # or else return empty list
    return shortestPath
