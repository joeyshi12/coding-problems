import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validate_bst(node: Node) -> bool:
    if node is None:
        return True
    if node.left and node.left.val > node.val:
        return False
    if node.right and node.right.val < node.val:
        return False
    return validate_bst(node.left) and validate_bst(node.right)

class TestValidateBST(unittest.TestCase):
    # TODO: add more tests
    def test_null(self):
        result = validate_bst(None)
        self.assertTrue(result)

    def test_invalid(self):
        root = Node(1, Node(2), Node(2))
        result = validate_bst(root)
        self.assertFalse(result)

    def test_valid(self):
        root = Node(1, Node(0), Node(2))
        result = validate_bst(root)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
