"""
You are given a list of tuples of the form [a, b, w] and a list of numbers weights,
where a, b are integers representing edges in a graph, w is the edge weight, and weights[i] is the weight of node i.

An assignment is a map from nodes to {+1, -1}.
Given an assignment, the graph objective is calculated as
the sum of all assignment[i] * weights[i] plus the sum of all w(a, b) * assignment[a] * assignment[b].

Find the assignment which minimizes the objective function.
"""

def find_minimum_assignment(edges: list[list[int]], node_weights: list[int]) -> list[int]:
    n = len(node_weights)
    min_objective = float("inf")
    min_assignment = []
    assignment = [-1] * n

    def calculate_objective(assignment: list[int]) -> int:
        return sum(assignment[i] * node_weights[i] for i in range(n)) + sum(w * assignment[a] * assignment[b] for a, b, w in edges)

    def backtrack(i: int):
        nonlocal min_objective
        nonlocal min_assignment
        if i >= n:
            return
        objective = calculate_objective(assignment)
        if objective < min_objective:
            min_objective = objective
            min_assignment = assignment.copy()
        for j in range(i, n):
            assignment[j] = 1
            backtrack(j + 1)
            assignment[j] = -1

    return min_assignment
