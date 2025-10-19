from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge

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
    """Print the DFS traversal of the graph starting from the start vertex"""

    #Set every vertex's visited_var to false
    #maybe create a new var with graph parameter
    start = start_vertex
    visited = [] #Will add visited vertices name to the list for end result
    visited_adj_list = Graph() #This is where the actual object adressesses will go for visited vertices
    


def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    raise NotImplementedError  


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