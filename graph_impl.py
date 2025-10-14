from graph_interfaces import IEdge, IGraph, IVertex
from typing import List, Protocol

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

class Graph(IGraph):
    def __init__(self):
        self.main_graph = {}
    def get_vertices(self) -> List[IVertex]: 
        return self.main_graph.keys()
    def get_edges(self) -> List[IEdge]: 
        #FINISH
        for vertex in range(self.main_graph):
            pass
        pass
    def add_vertex(self, vertex: IVertex) -> None: 
        #DOUBLE CHECK!!
        Vertex.set_name(vertex)
        self.main_graph[vertex]= []
    def remove_vertex(self, vertex_name: str) -> None: 
        self.main_graph.pop(vertex_name)
    def add_edge(self, vertex1, vertex2) -> None: 
        Vertex.add_edge(self.main_graph,vertex1,vertex2)
    def remove_edge(self, vertex1, vertex2) -> None: 
        Vertex.remove_edge(self, vertex1, vertex2)



class Vertex(IVertex):
    def _init_(self):
        self._visited = False
        self._name = None
    def get_name(self) -> str: 
        return self._name
    def set_name(self, name: str) -> None:
        self._name = name
    def add_edge(self, graph, vertex1, vertex2) -> None: 
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    def remove_edge(self, graph, vertex1, vertex2) -> None:
        graph[vertex1].remove(vertex2)
        graph[vertex2].remove(vertex1)
    def get_edges(self) -> List[IEdge]: 
        pass
    def set_visited(self, visited: bool) -> None: 
        self._visited = True
    def is_visited(self) -> bool: 
        return self._visited

class Edge(IEdge):
    def get_name(self) -> str: 
        pass
    def set_name(self, name: str) -> None: 
        pass
    def get_destination(self) -> IVertex: 
        pass
    def get_weight(self) -> float: 
        pass
    def set_weight(self, weight: float) -> None:
        pass
