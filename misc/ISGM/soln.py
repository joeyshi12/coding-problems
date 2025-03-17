"""
Given an undirected graph G = (V,E) with vertices V and edges E,
an integer (positive, zero, or negative) weight h_v for each v∈ V,
and an integer (positive, zero, or negative) weight J_{u,v} for each edge {u,v}∈ E,
find an assignment of +1 or −1 to the variables x_v for each v∈ V
that minimizes the objective function:

(sum_{v∈ V} h_v*x_v) + (sum_{(u,v)∈ E} J_{u,v} * x_u * x_v)
"""

from typing import List, Dict

class Node:
    def __init__(self, weight, edges=None):
        self.weight = weight
        self.edges = edges if edges else []

class Edge:
    def __init__(self, weight, dest):
        self.weight = weight
        self.dest = dest

def assign(graph: List[Node]) -> Dict[Node, int]:
    # TODO: add tests + implement
    assignment = {node: -1 for node in graph}
    return assignment

def obj_func(graph: List[Node], assignment: Dict[Node, int]) -> int:
    obj_val = sum(node.weight * assignment[node] for node in graph)
    visited = set()
    for node in graph:
        for edge in node.edges:
            if edge.dest not in visited:
                obj_val += edge.weight * assignment[node] * assignment[node.dest]
        visited.add(node)
    return obj_val
