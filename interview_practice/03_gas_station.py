"""
Problem 2.1: Greedy -- Gas Station

You have n gas stations on a circular route. Station i has gas[i]
fuel and it costs cost[i] to travel from station i to i + 1. Find a
starting station that allows a full circuit, or return -1 if none
exists.

Goal: O(n) greedy solution. Be ready to explain why the greedy
approach works.
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    Return the index of the starting gas station that allows a full
    circuit of the route, or -1 if no such station exists.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert can_complete_circuit(gas, cost) == 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert can_complete_circuit(gas, cost) == -1

    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    assert can_complete_circuit(gas, cost) == 4

    print("All basic checks passed.")
