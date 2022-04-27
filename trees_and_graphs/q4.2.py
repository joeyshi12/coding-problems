import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_minimal_tree(nums):
    if not nums:
        return None
    return create_minimal_tree_helper(nums, 0, len(nums) - 1)

def create_minimal_tree_helper(nums, start, end):
    if start > end:
        return None
    m = (start + end + 1) // 2
    node = Node(nums[m])
    node.left = create_minimal_tree_helper(nums, start, m - 1)
    node.right = create_minimal_tree_helper(nums, m + 1, end)
    return node

class TestCreateMinimalTree(unittest.TestCase):
    # TODO: add more test cases
    def test_empty(self):
        result = create_minimal_tree([])
        self.assertEqual(result, None)

    def test_non_trivial(self):
        nums = [0, 1, 2, 3, 4, 5, 6]
        result = create_minimal_tree(nums)
        self.assertIsBinarySearchTree(result)

    def assertIsBinarySearchTree(self, node):
        if not node:
            return
        if node.left:
            self.assertTrue(node.left.val < node.val)
            self.assertIsBinarySearchTree(node.left)
        if node.right:
            self.assertTrue(node.val < node.right.val)
            self.assertIsBinarySearchTree(node.right)

if __name__ == "__main__":
    unittest.main()
