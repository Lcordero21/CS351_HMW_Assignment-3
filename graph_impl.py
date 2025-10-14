from graph_interfaces import IEdge, IGraph, IVertex
from typing import Dict, List, Protocol

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

class Graph(IGraph):
    def __init__(self):
        self._adj_list: Dict[str, List[str]] = {}

    def get_vertices(self) -> List[IVertex]: 
        pass
    def get_edges(self) -> List[IEdge]: 
        pass
    def add_vertex(self, vertex: IVertex) -> None: 
        pass
    def remove_vertex(self, vertex_name: str) -> None: 
        pass
    def add_edge(self, vertex1, vertex2) -> None: 
        pass
    def remove_edge(self, vertex1, vertex2) -> None: 
        pass



class Vertex(IVertex):
    def _init_(self, name):
        self._visited: bool = False
        self._name: str = name
        self._edges: List[IEdge] = []

    def get_name(self) -> str: 
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name

    def add_edge(self, edge) -> None: 
        self._edges.append(edge)

    def remove_edge(self, edge_name) -> None:
        for edge in self._edges:
            if edge.get_name() == edge_name:
                self._edges.remove(edge)
                return
            
    def get_edges(self) -> List[IEdge]: 
        return self._edges

    def set_visited(self, visited: bool) -> None: 
        self._visited = visited

    def is_visited(self) -> bool: 
        return self._visited

class Edge(IEdge):
    def __init__(self, name: str, destination) -> None:
        self._name: str = name
        self._destination = destination
        self._is_bi_directional: bool = False
        self._weight: float = None
    def get_name(self) -> str: 
        return self._name
    def set_name(self, name: str) -> None: 
        self._name = name
    def get_destination(self) -> IVertex: 
        return self._destination
    def get_weight(self) -> float: 
        return self._weight
    def set_weight(self, weight: float) -> None:
        self._weight = weight
