class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."

def numShortestPaths(g, start, end):
	"""graph, start node, end node -> int
	Purpose: find the number of shortest paths between two nodes in a graph
	Raises: raise InvalidInputException if an input is None, or 
	if start or end are not in g"""
