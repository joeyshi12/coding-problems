import unittest
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_bst(node: Node) -> bool:
    return is_bst(node, None, None)


def is_bst(node: Node, lower: Optional[int], upper: Optional[int]) -> bool:
    if node is None:
        return True
    if node.left:
        if lower and node.left.val < lower:
            return False
        if node.val < node.left.val:
            return False
    if node.right:
        if upper and node.right.val > upper:
            return False
        if node.val > node.right.val:
            return False
    return is_bst(node.left, lower, node.val) and is_bst(node.right, node.val, upper)


class TestValidateBST(unittest.TestCase):
    # TODO: add more tests
    def test_null(self):
        result = validate_bst(None)
        self.assertTrue(result)

    def test_invalid(self):
        root = Node(1, Node(0, right=Node(2)), Node(2))
        result = validate_bst(root)
        self.assertFalse(result)

    def test_valid(self):
        root = Node(1, Node(0), Node(2))
        result = validate_bst(root)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
