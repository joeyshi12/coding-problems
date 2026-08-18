"""
Problem 2.5: Trees -- Bid Hierarchy Rollup

Given a tree of campaign -> ad group -> ad, where each leaf has a bid
amount, compute the total and average bid at every level as a nested
summary.

Goal: clean recursive traversal with aggregation, plus a clear
complexity explanation.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Node:
    name: str
    bid: Optional[float] = None       # only set on leaf (ad) nodes
    children: List["Node"] = field(default_factory=list)


@dataclass
class Summary:
    name: str
    total_bid: float
    average_bid: float
    children: List["Summary"] = field(default_factory=list)


def rollup(node: Node) -> Summary:
    """
    Recursively compute total and average bid for this node and all
    descendants, returning a nested Summary tree.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------
# Quick manual tests -- replace / extend as you implement
# ---------------------------------------------------------------------

if __name__ == "__main__":
    tree = Node(
        name="Campaign A",
        children=[
            Node(
                name="Ad Group 1",
                children=[
                    Node(name="Ad 1", bid=2.0),
                    Node(name="Ad 2", bid=4.0),
                ],
            ),
            Node(
                name="Ad Group 2",
                children=[
                    Node(name="Ad 3", bid=6.0),
                ],
            ),
        ],
    )

    summary = rollup(tree)
    assert summary.total_bid == 12.0
    assert summary.average_bid == 4.0

    group1 = summary.children[0]
    assert group1.total_bid == 6.0
    assert group1.average_bid == 3.0

    print("All basic checks passed.")
