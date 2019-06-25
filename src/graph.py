class Grafo(object):

    __slots__ = ['__graph_dict']

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        if vertex1 in self.__graph_dict:
            if vertex2 not in self.__graph_dict[vertex1]:
                self.__graph_dict[vertex1].append(vertex2)
                return 1
            else:
                return 0
        else:
            self.__graph_dict[vertex1] = [vertex2]
            return 2
    
    def find_node(self, nome):
        for vertice in self.__graph_dict:
            if vertice.nome == nome:
                return vertice

            for v in self.__graph_dict[vertice]:
                if v.nome == nome:
                    return v
        
        return None
    
    def get_info(self, nome):
        for v in self.__graph_dict:
            if v.nome == nome:
                return v, len(self.__graph_dict[v])
        
        return None, 0

"""
graph.add_vertex("z")
graph.add_edge({"a","z"})
"""