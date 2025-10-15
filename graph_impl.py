from graph_interfaces import IEdge, IGraph, IVertex
from typing import Dict, List, Protocol, TypeVar, Tuple, Optional

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

T= TypeVar('T')

class Graph[T](IGraph[T]):
    def __init__(self):
        self._adj_list: Dict[str, List[str]] = {}
        self._vertices: List[IVertex] = []

    def get_vertices(self) -> List[IVertex]: 
        return self._vertices

    def get_edges(self) -> List[IEdge]: 
        return Vertex.get_edges()

    def add_vertex(self, vertex: IVertex) -> None: 
        self._vertices.append(Vertex(vertex))

    def remove_vertex(self, vertex_name: str) -> None: 
        pass

    def add_edge(self, edge: IEdge, from_vertex_name: str, to_vertex_name: str) -> None: 
        from_vertex = None
        to_vertex = None

        for vertex in self._vertices:
            if vertex.get_name() == from_vertex_name:
                from_vertex = vertex

            if vertex.get_name() == to_vertex_name:
                to_vertex = vertex
        
        if from_vertex is None or to_vertex is None:
            raise Exception("One or more of the vertexes do not exist")

        the_edge = Edge(edge, to_vertex)
        from_vertex.add_edge(the_edge)

        second_edge = Edge(edge, from_vertex)
        to_vertex.add_edge(second_edge)

    def remove_edge(self, edge_name: str) -> None: 
        pass



class Vertex(IVertex):
    def _init_(self, name):
        self._visited: bool = False
        self._name: str = name
        self._edges: List[IEdge] = []
        self._data: Optional[T] = None
        self._coordinates: Tuple[float,float] = (0,0)

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
