"""
Problem 2.2: Graph / BFS -- Campaign Reach Simulation

Model ad placements as a graph, with edges representing shared
audience overlap. Given a start node and a hop limit, return all
reachable placements.

Extension: weight edges by overlap cost and find the cheapest path to
a target within the hop limit.

Goal: BFS for the base case, then a Dijkstra style bounded search for
the extension.
"""

from collections import deque
from typing import Dict, List, Set
import heapq


# Base case: unweighted graph, adjacency list of placement -> neighbors
Graph = Dict[str, List[str]]

# Extension: weighted graph, adjacency list of
# placement -> list of (neighbor, cost)
WeightedGraph = Dict[str, List[tuple]]


def reachable_within_hops(graph: Graph, start: str, max_hops: int) -> Set[str]:
    """
    Return the set of placements reachable from start within max_hops
    edges (not including start itself, unless you decide otherwise --
    state your assumption).
    """
    raise NotImplementedError


def cheapest_path_within_hops(
    graph: WeightedGraph, start: str, target: str, max_hops: int
) -> float:
    """
    Return the minimum total cost to reach target from start using at
    most max_hops edges. Return float('inf') if unreachable within the
    hop limit.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
    }

    assert reachable_within_hops(graph, "A", 1) == {"B", "C"}
    assert reachable_within_hops(graph, "A", 2) == {"B", "C", "D"}
    assert reachable_within_hops(graph, "A", 3) == {"B", "C", "D", "E"}

    weighted_graph = {
        "A": [("B", 2), ("C", 5)],
        "B": [("A", 2), ("D", 1)],
        "C": [("A", 5), ("D", 1)],
        "D": [("B", 1), ("C", 1), ("E", 3)],
        "E": [("D", 3)],
    }

    # A -> B -> D costs 3, within 2 hops
    assert cheapest_path_within_hops(weighted_graph, "A", "D", 2) == 3
    # A -> B -> D -> E costs 6, needs 3 hops
    assert cheapest_path_within_hops(weighted_graph, "A", "E", 2) == float("inf")
    assert cheapest_path_within_hops(weighted_graph, "A", "E", 3) == 6

    print("All basic checks passed.")
