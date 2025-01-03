from typing import Dict, Optional
import unittest

class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def check_balanced(root: Node) -> bool:
    heights = {}
    compute_heights(root, heights)
    return check_balanced_helper(root, heights)

def compute_heights(node: Optional[Node], heights: Dict[Node, int]) -> int:
    if node is None:
        return 0

    if node.left and node.left not in heights:
        heights[node.left] = compute_heights(node.left, heights)
    if node.right and node.right not in heights:
        heights[node.right] = compute_heights(node.right, heights)

    if node.left is None and node.right is None:
        heights[node] = 0
    else:
        left_height = heights.get(node.left, 0)
        right_height = heights.get(node.right, 0)
        heights[node] = max(left_height, right_height) + 1

    return heights[node]

def check_balanced_helper(node: Optional[Node], heights: Dict[Node, int]) -> bool:
    if node is None:
        return True
    left_height = heights.get(node.left, 0)
    right_height = heights.get(node.right, 0)
    return abs(left_height - right_height) < 2

class TestCheckBalanced(unittest.TestCase):
    # TODO: add more tests
    def test_null(self):
        result = check_balanced(None)
        self.assertTrue(result)

    def test_imbalanced(self):
        root = Node("A", Node("B"), Node("C", Node("D", Node("E"))))
        result = check_balanced(root)
        self.assertFalse(result)

    def test_balanced(self):
        root = Node("A", Node("B"), Node("C", Node("D")))
        result = check_balanced(root)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

