from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge
import copy

def read_graph(file_path: str) -> IGraph:  
    """Read the graph from the file and return the graph object"""
    temp_graph = Graph()
    with open(file_path) as paths:
        for line in paths:
            origin, destination, highway, distance = line.split(",")
            if origin != "source":
                temp_graph.add_vertex(origin)
                temp_graph.add_vertex(destination)
                temp_graph.add_edge(highway, origin, destination, distance)
    return temp_graph

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """
        Print the DFS traversal of the graph starting from the start vertex (I used the iterative 
        approach)
    """

    stack = []
    visited = []
    visited_adj_list = Graph()

    stack.append(start_vertex)

    while len(stack) is not 0:
        vertex = stack.pop()
        if vertex.is_visited() == False:
            visited_adj_list.add_vertex(vertex)
            visited.append(vertex.get_name())
            vertex.set_visited(True)
            for edge in vertex.get_edges():
                stack.append(edge.get_destination())

    reset_visited(visited_adj_list.get_vertices())

    print(visited)



def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """
        Print the BFS traversal of the graph starting from the start vertex (I used the 
        iterative approach)
    """

    queue = []
    visited = []
    visited_adj_list = Graph()

    queue.append(start_vertex)
    visited.append (start_vertex.get_name())
    visited_adj_list.add_vertex(start_vertex)

    while len(queue) is not 0:
        vertex = queue.pop(0)
        if vertex.is_visited() == False:
            visited_adj_list.add_vertex(vertex)
            visited.append(vertex.get_name())
            vertex.set_visited(True)
            for edge in vertex.get_edges():
                queue.append(edge.get_destination())

    
    reset_visited (visited_adj_list.get_vertices())

    print(visited)

def reset_visited(graph:IGraph) -> None:
    """
    Purpose: 
        Resets all the visited statuses of the each vertex in a graph.
    """
    for vertex in graph:
        vertex.set_visited(False)


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    for i in graph.get_vertices():
        print(i.get_name())
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()