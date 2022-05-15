# https://leetcode.com/problems/deepest-leaves-sum/

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepest_leaves_sum(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    level = [root]
    previous_level = []
    while level:
        level, previous_level = [], level
        for node in previous_level:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
    return sum(node.val for node in previous_level)


class TestDeepestLeavesSum(unittest.TestCase):
    def test_null(self):
        result = deepest_leaves_sum(None)
        self.assertEqual(result, 0)

    def test_leaf(self):
        root = TreeNode(1)
        result = deepest_leaves_sum(root)
        self.assertEqual(result, 1)

    def test_left_child(self):
        root = TreeNode(1, left=TreeNode(2))
        result = deepest_leaves_sum(root)
        self.assertEqual(result, 2)

    def test_right_child(self):
        root = TreeNode(1, right=TreeNode(2))
        result = deepest_leaves_sum(root)
        self.assertEqual(result, 2)

    def test_large_tree(self):
        n7 = TreeNode(7)
        n4 = TreeNode(4, left=n7)
        n5 = TreeNode(5)
        n2 = TreeNode(2, left=n4, right=n5)

        n8 = TreeNode(8)
        n6 = TreeNode(6, right=n8)
        n3 = TreeNode(3, right=n6)

        root = TreeNode(1, left=n2, right=n3)
        result = deepest_leaves_sum(root)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
