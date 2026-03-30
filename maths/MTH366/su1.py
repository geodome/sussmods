from typing import List, Dict, Set

AdjList = Dict[str, Set[str]]

def find_spanning_tree(graph: AdjList) -> List[AdjList]:
    """
    This function constructs a series of spanning tree which are 
    subgraphs of the given graph
    * graph: adjacency list expressing the graph
    """
    def bfs_tree(start:str, visited:Set[str], graph:AdjList) -> AdjList:
        """
        the breath first search algorithm is used to construct a spanning tree
        from the given graph
        * start: the label of the root vertex
        * visited: the set of vertices that have been visited
        * graph: an adjacency list that describes the graph
        """
        queue = [start]
        tree: AdjList = dict()
        while len(queue) > 0:
            current = queue.pop(0)
            visited.add(current)
            tree[current] = set()
            for v in graph[current]:
                if v not in visited:
                    queue.append(v)
                    tree[current].add(v)
                    if v not in tree:
                        tree[v] = set()
                    tree[v].add(current)
        return tree    
    visited: Set[str] = set()
    trees:List[AdjList] = []
    for vertex in graph.keys():
        if vertex not in visited:
            tree = bfs_tree(vertex, visited, graph)
            trees.append(tree)
    return trees
