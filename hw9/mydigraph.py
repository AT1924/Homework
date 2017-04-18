class NoSuchEdgeException(Exception):
    """This exception is raised when, even though all the edges/vertices
    passed in are valid, there is still no way to retrieve
    the edge requested"""
    pass

class NoSuchVertexException(Exception):
    """This exception is raised when, even though all the edges/vertices
    passed in are valid, there is still no way to retrieve
    the vertex requested"""
    pass

class InvalidEdgeException(Exception):
    """This exception is raised when an edge itself that is passed in
    is not an edge in the graph when it is supposed to be, or vice-versa,
    or is None"""
    pass

class InvalidVertexException(Exception):
    """This exception is raised when a vertex itself that is passed in
    is not a vertex in the graph when it is supposed to be, or vice-versa,
    or is None"""
    pass

class GraphException(Exception):
    """This exception is raised when performing some action would corrupt
    the structure of the graph"""
    pass
    
class ElementHolder(object):
    """This is a base class for any object that needs to contain or
    reference element (some generic object).
    
    Note that the ElementHolder will _always_ contain the object, so
    in a sense an ElementHolder is immutable."""
    __nextId = 0
    
    def __init__(self, element):
        """Constructs the object, with ELEMENT being the object that this
        will contain."""
        self.__element = element
        self.__id = self.__class__.__nextId
        self.__class__.__nextId += 1
    
    def __eq__(self, other):
        """Tests equality. The key thing to note is that two ElementHolders
        are equal if they have the same ID, _not_ if they contain the same
        object (since the ElementHolder class is an abstraction for a container;
        we are comparing whether two containers are the same, but different
        containers can contain the same object)"""
        return self.id() == other.id()
    
    def __ne__(self, other):
        """Tests non-equality"""
        return not self == other
    
    def __hash__(self):
        """We hash based on the identifier, because this completely
        determines the ElementHolder."""
        return hash(self.id())
    
    def element(self):
        """Gets the element that this object holds."""
        return self.__element
    
    def copy(self):
        """Returns a shallow copy of this ElementHolder, meaning that only
        the object reference gets copied."""
        tmp = ElementHolder(self.element())
        tmp.__id = self.id()
        return tmp
    
    def id(self):
        """Returns an identifier number for the ElementHolder. The ID is all
        that determines the uniqueness of an ElementHolder. """
        return self.__id
        
class GraphVertex(ElementHolder):
    """Class that represents a vertex in a graph. A vertex can have an
    object associated with it (e.g. a weight), hence the reason from
    inheriting from ElementHolder."""
    def __str__(self):
        """Prints the vertex, giving information on the vertex itself and
        the element it contains."""
        return "Vertex #" + str(self.id()) + ": " + str(self.element())

class GraphEdge(ElementHolder):
    """Class that represents an edge in a graph. An edge can have an
    object associated with it (e.g. a weight), hence the reason from
    inheriting from ElementHolder."""
    def __str__(self):
        """Prints the edge, giving information on the vertex itself and
        the element it contains."""
        return "Edge #" + str(self.id()) + ": " + str(self.element())

class MyDigraph(object):
    """Class that represents a directed graph based on gbressle's MyGraph, with adjacency-matrix big-O times.
    
        Some notes about implementation:
        1) We implement the adjacency matrix not as an actual 2D array,
        but as a hash table of hash tables (in PythonSpeak, a dictionary
        of dictionaries). There are four main reasons for this:
            a) the code is cleaner; with a true 2D array there's a lot of bookkeeping to do
            b) it's more \"pythonesque\"
            c) 2D arrays would have to be of a fixed size unless you want to add a lot of ugly code
            d) it has the same big-O runtime for access, insertion, etc.
        2) Instead of storing the edges and vertices in some sort of linked list, we use a
        cleaner implementation: a set (which is basically a dictionary without the values).
        This makes perfect sense considering the mathematical representation of a graph
        (and has the same big-O time as a linked list for the operations we need:
        insertion is O(1), iteration is O(n)
        3) insertVertex() and insertEdge() actually take _vertices_ and _edges_
        as arguments, not elements from which vertices and edges are created. This allows
        you to have a vertex or edge in more than one graph (and you don't need to make
        them have the same connections in both graphs; it's just like the mathematical
        idealization of a graph)."""
        
    def __init__(self):
        """Initializes a blank graph."""
        self.clear()
    
    def __str__(self):
        """Returns a string representation of this graph, giving all the vertices, edges,
        the connections between them, and the associated elements."""
        sList = ["verts = "]
        for v in self.vertices():
            sList.append("(#" + str(v.id()) + " : " + str(v.element()) + ") ")
        s = ''.join(sList)
        sList = [s, "\nedges = "]
        for e in self.edges():
            a = self.endVertices(e)
            sList.append("(" + str(e.element()) \
                         + ": (#" + str(a[0].id()) + ", #" + str(a[1].id()) + ")) ") 
        s = ''.join(sList)
        return s
    
    def areAdjacent(self, v1, v2):
        """areAdjacent: GraphVertex * GraphVertex -> bool
        Consumes: two vertices contained in this graph
        Produces: a boolean whether V1 has a directed edge to V2 in this graph
        Example: areAdjacent(v1,v2) -> True (if v1->v2 exists in this graph)
        
        Throws InvalidVertexException if a vertex isn't in the graph.
        
        Runs in O(1)."""
        self.__testVertex(v1)
        self.__testVertex(v2)
        return (v1 in self.__adjMatrix and v2 in self.__adjMatrix[v1] and self.__adjMatrix[v1][v2] is not None)
    
    def insertVertex(self, v):
        """insertVertex: GraphVertex -> GraphVertex
        Consumes: a vertex not already contained in this graph
        Produces: a vertex that has just been added to the graph
        Purpose: adds a vertex to this graph
        Example: insertVertex(GraphVertex('a')) -> GraphVertex('a') provided 'a' is not contained in this graph
            
        Throws InvalidVertexException if the vertex is already in the graph.
        
        Runs in O(1)."""
        self.__testVertex(v, wantInGraph=False, wantNotInGraph=True)

        self.__vertices.add(v)
        return v
    
    def insertEdge(self, v1, v2, e):
        """insertEdge: GraphVertex * GraphVertex * GraphEdge -> GraphEdge
        Consumes: two vertices contained in this graph and an edge that is not contained in this graph
        Produces: an edge from v1 to v2 that has just been added to this graph
        Purpose: Add an edge from v1 pointing towards v2 to this graph
        Example: insertEdge(v1,v2, GraphEdge('T')) -> GraphEdge('T') (provided there is no edge v1->v2 in this graph)
        
        Throws InvalidEdgeException if the edge is already in the graph.
        Throws InvalidVertexException if either vertex is _not_ in the graph.
        Throws GraphException if this insertion would make the graph non-simple.
        
        Runs in O(1)."""
        self.__testVertex(v1)
        self.__testVertex(v2)
        self.__testEdge(e, wantInGraph=False, wantNotInGraph=True)
        
        if v1 == v2:
            raise GraphException("can't have a vertex connected to itself")
        
        if self.areAdjacent(v1, v2):
            raise GraphException("vertices already have edge connecting them")
        
        self.__edges.add(e)
        if v1 not in self.__adjMatrix:
            self.__adjMatrix[v1] = {}
        self.__adjMatrix[v1][v2] = e
            
        e.fromVertex = v1
        e.toVertex = v2
        
        return e

    def removeVertex(self, v):
        """removeVertex: GraphVertex -> element
        Consumes: a vertex contained in this graph
        Produces: the element of the vertex that has just been removed from this graph
        Purpose: Removes vertex v from the graph
        Side Effects: it will also remove any edge that is connected to the vertex
        
        Throws InvalidVertexException if the vertex is not in the graph.
        
        Runs in O(|V|)."""
        
        self.__testVertex(v)
        
        for w in self.__vertices:
            if self.areAdjacent(v, w):
                self.removeEdge(self.connectingEdge(v, w))
        
        self.__vertices.remove(v)
        return v.element()
    
    def removeEdge(self, e):
        """removeEdge: GraphEdge -> element
        Consumes: an edge contained in this graph
        Produces: the element of the edge that has just been removed from this graph
        Purpose: Removes edge e from the graph
        Side Effects: it will also remove any edge that is connected to the vertex
        
        Throws InvalidEdgeException if the edge is not in the graph.
        
        Runs in O(1)."""
        
        self.__testEdge(e)
        a = self.endVertices(e)

        self.__edges.remove(e)

        self.__adjMatrix[a[0]][a[1]] = None
        
        return e.element()
    
    def connectingEdge(self, v1, v2):
        """connectingEdge: GraphVertex * GraphVertex -> GraphEdge
        Consumes: two vertices contained in this graph
        Produces: the edge connecting v1 -> v2
        Purpose: returns the edge extending from v1 to v2
        
        Throws InvalidVertexException if either vertex is not in the graph.
        Throws NoSuchEdgeException if there is no edge in the graph that connects these vertices.
        
        Runs in O(1)."""
        self.__testVertex(v1)
        self.__testVertex(v2)
        
        if not self.areAdjacent(v1, v2):
            raise NoSuchEdgeException("there is no edge between these vertices")
        
        return self.__adjMatrix[v1][v2]
    
    def incidentEdges(self, v):
        """incidentEdges: GraphVertex -> list
        Consumes: vertex contained in this graph
        Produces: a list of edges whose endpoint is vertex v (pointing towards v)
        Purpose: returns a list of edges incident on vertex v
        Returns a list of the edges which point _to_ a vertex v. Note that this is slightly different from the definition of "incident" for directionless graphs.  
        
        Throws InvalidVertexException if the vertex is not in the graph.
        
        Runs in O(|V|)."""
        self.__testVertex(v)
        
        return [self.connectingEdge(w, v) for w in self.__vertices if w != v and self.areAdjacent(w, v)]

    def emanantEdges(self, v):
        """emanantEdges: GraphVertex -> list
        Consumes: vertex contained in this graph
        Produces: a list of edges pointing away from v
        Purpose: returns a list of edges emanating from vertex v
        
        Throws InvalidVertexException if the vertex is not in the graph. 

        Runs in O(|V|)."""
        self.__testVertex(v)

        return[self.connectingEdge(v, w) for w in self.__vertices if w != v and self.areAdjacent(v, w)]

    def allEdges(self,v):
        """allEdges: GraphVertex -> list
        Consumes: vertex contained in this graph
        Produces: a list of edges that either start or end on vertex v
        Purpose: returns a list of all edges on which a vertex v lies, regardless of orientation. 

        Throws InvalidVertexException if the vertex is not in the graph.

        Runs in O(|V|)."""
        self.__testVertex(v)

        return[self.incidentEdges(v)+self.emanantEdges(v)]
                
    def opposite(self, v, e):
        """opposite: GraphVertex * GraphEdge -> GraphVertex
        Consumes: vertex contained in this graph and an edge that either starts or end on vertex v
        Produces: a vertex opposite of vertex v on edge e
        Purpose: returns the vertex opposite of v on edge e
        
        Throws InvalidVertexException if the vertex is not in the graph.
        Throws InvalidEdgeException if the edge is not in the graph.
        Throws NoSuchVertexException if the vertex is not on the edge (so the request doesn't make sense).
        
        Runs in O(1)."""
        self.__testVertex(v)
        self.__testEdge(e)
        
        if e.toVertex == v:
            return e.fromVertex
        elif e.fromVertex == v:
            return e.toVertex
        else:
            raise NoSuchVertexException("vertex is not on edge")
    
    def endVertices(self, e):
        """endVertices: GraphEdge -> list
        Consumes: edge contained in this graph
        Produces: a list of two vertices
        Purpose: returns the endpoint vertices of edge e, ordered: [fromVertex, toVertex]
        
        Throws InvalidEdgeException if the edge is not in the graph.
        
        Runs in O(1)."""
        self.__testEdge(e)
        
        return [e.fromVertex, e.toVertex]
            
    def edges(self):
        """edges: . -> list
        Consumes: nothing
        Produces: a list of edges
        Purpose: returns a list of all edges in the graph regardless of orientation
        
        Runs in O(|V|^2) (we need to create a new set of edges; we don't)
        want the caller to be able to screw up the original set)."""
        return set(self.__edges)
    
    def vertices(self):
        """edges: . -> list
        Consumes: nothing
        Produces: a list of vertices
        Purpose: returns a list of all vertices in this graph
        
        Runs in O(|V|) (we need to create a new set of vertices; we don't)
        want the caller to be able to screw up the original set)."""
        return set(self.__vertices)
    
    def iterEdges(self):
        """iterEdges: . -> iterator
        Consumes: nothing
        Produces: an iterator of edges
        Purpose: returns an iterator of all edges in this graph regardless of orientation
        
        This is like edges(), except that it returns just an iterator
        for the edges. This gives better performance, if we
        just need to iterate through the edges and don't need a full copy
        of the edges.
        
        Runs in O(1)."""
        
        return iter(self.__edges)
    
    def iterVertices(self):
        """iterVertices: . -> iterator
        Consumes: nothing
        Produces: an iterator of vertices
        Purpose: returns an iterator of all vertices in this graph
        
        This is like vertices(), except that it returns just an iterator
        for the vertices. This gives better performance, if we
        just need to iterate through the edges and don't need a full copy
        of the vertices.
        
        Runs in O(1)."""
        
        return iter(self.__vertices)
    
    def containsEdge(self, e):
        """containsEdge: GraphEdge -> bool
        Consumes: an edge contained in the graph
        Produces: a boolean
        Purpose: returns True if edge e is in contained in this graph
        
        Runs in O(1)."""
        
        return e in self.__edges
    
    def containsVertex(self, v):
        """containsVertex: GraphVertex -> bool
        Consumes: a avertex contained in the graph
        Produces: a boolean
        Purpose: returns True if ertex v is in contained in this graph
        
        Runs in O(1)."""
        
        return v in self.__vertices

    def copy(self):
        """copy: . -> MyDigraph
        Consumes: nothing
        Produces: an instance of MyDigraph
        Purpose: Returns an identical copy of this graph

        Runs in O(|V|+|E|)."""

        copy=MyDigraph()
        vertex_to_copy = {}
        for v in self.vertices():
            w=v.copy()
            vertex_to_copy[v] = w
            copy.insertVertex(w)
        for e in self.edges():
            f=e.copy()
            a=self.endVertices(e)
            v1 = vertex_to_copy[a[0]]
            v2 = vertex_to_copy[a[1]]
            copy.insertEdge(v1, v2, e)
        return copy
    
    def clear(self):
        """clear: . -> .
        Consumes: nothing
        Produces: nothing
        Purpose: clears all edges and vertices from this graph
        """
        self.__edges = set()
        self.__vertices = set()
        self.__adjMatrix = {}
        
    def __testVertex(self, v, wantInGraph = True, wantNotInGraph=False):
        """Helper function that tests the \"validity\" of a vertex. A vertex
        is invalid if:
            1) it is None
            2) the calling method would add a vertex that is already in the graph.
            3) a vertex is requested which is not in the graph but must be for the method to work.
        """
        if v is None:
            raise InvalidVertexException("vertex is None")

        if wantInGraph and v not in self.__vertices:
            raise InvalidVertexException("vertex is not in this graph")
        elif wantNotInGraph and v in self.__vertices:
            raise InvalidVertexException("vertex is already in this graph")
        
    def __testEdge(self, e, wantInGraph = True, wantNotInGraph=False):
        """Helper function that tests the \"validity\" of an edge. An edge
        is invalid if:
            1) it is None
            2) the calling method would add an edge that is already in the graph.
            3) an edge is requested which is not in the graph but must be for the method to work.
        """
        if e is None:
            raise InvalidEdgeException("edge is None")
            
        if wantInGraph and e not in self.__edges:
            raise InvalidEdgeException("edge is not in this graph")
        elif wantNotInGraph and e in self.__edges:
            raise InvaildEdgeException("edge is already in this graph")
    
    def graphicVisit(self, f1, f2):
        from Queue import Queue
        
        vertices = self.iterVertices()
        for v in vertices:
            v.visited = False
        
        edges = self.iterEdges()
        for e in edges:
            e.visited = False
        
        vertices = self.iterVertices()
        for u in vertices:
            if not u.visited:
                Q = Queue()
                Q.put(u)
                while not Q.empty():
                    v = Q.get()
                    if v.visited:
                        continue
                    f1(v)
                    v.visited = True
                    for e in self.incidentEdges(v):
                        if not e.visited:
                            e.visited = True
                            f2(e)
                            ov = self.opposite(v, e)
                            Q.put(ov)
                        
    def graphic(self):
        """Returns a representation of this graph as a .dot file.

        In other words, if you pass the string returned by this method into
        the program DOT (or, better yet, NEATO), you can get an image file
        of the graph."""
        self.strs = ["graph\n{\n"]
        
        def annex_vertex(v):
            self.strs.append("\t" + str(v.element()) + " [label=\"" \
                        + str(v.element()) + "\"];\n")

        def annex_edge(e):
            a = self.endVertices(e)
            self.strs.append("\t" + str(a[0].element()) + " -- " + str(a[1].element())\
                             + " [label=\"" \
                             + " " + str(e.element()) + "\" dir=forward];\n")

        self.graphicVisit(annex_vertex, annex_edge)
        self.strs.append("}\n")
        if len(self.strs) == 2:
            return None
        return ''.join(self.strs)

    def popup(self):
        """Opens a new window with this graph rendered by DOT.
        Sequential calls to this function will show the window
        once at a time. """
        import os
        tmp = open("./.tmpgraph", "w+")
        graph = self.graphic()
        if graph == None:
            print 'error in generating graph :('
            return
        tmp.write(self.graphic())
        tmp.close()
        os.system("dot -Tpng ./.tmpgraph | display")
