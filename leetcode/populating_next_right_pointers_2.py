# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

import unittest


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Node) -> Node:
    if root is None:
        return None
    if root.left and root.right:
        root.left.next = root.right
    if root.right:
        root.right.next = find_next(root.next)
    elif root.left:
        root.left.next = find_next(root.next)
    connect(root.right)
    connect(root.left)
    return root


def find_next(root: Node) -> Node:
    if root is None:
        return None
    if root.left:
        return root.left
    if root.right:
        return root.right
    return find_next(root.next)


class TestConnect(unittest.TestCase):
    def test_null(self):
        result = connect(None)
        self.assertIsNone(result)

    def test_single(self):
        root = Node()
        result = connect(root)
        self.assertEqual(root, result)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
        self.assertIsNone(root.next)

    def test_two_levels(self):
        left = Node(val=2)
        right = Node(val=3)
        root = Node(val=1, left=left, right=right)
        result = connect(root)
        self.assertEqual(result, root)
        self.assertIsNone(result.next)
        self.assertEqual(left.next, right)
        self.assertIsNone(right.next)

    def test_multi_level(self):
        n4 = Node(val=4)
        n5 = Node(val=5)
        n7 = Node(val=7)
        n2 = Node(val=2, left=n4, right=n5)
        n3 = Node(val=3, right=n7)
        root = Node(val=1, left=n2, right=n3)
        result = connect(root)
        self.assertEqual(result, root)

        self.assertEqual(n2.next, n3)
        self.assertIsNone(n3.next)

        self.assertEqual(n4.next, n5)
        self.assertEqual(n5.next, n7)
        self.assertIsNone(n7.next)

    def test_1(self):
        n7 = Node(val=7)
        n8 = Node(val=8)
        n9 = Node(val=9)
        n10 = Node(val=10)

        n4 = Node(val=4, left=n7, right=n8)
        n5 = Node(val=5, left=n9, right=n10)
        n6 = Node(val=6)

        n2 = Node(val=2, left=n4)
        n3 = Node(val=3, left=n5, right=n6)

        root = Node(val=1, left=n2, right=n3)
        result = connect(root)
        self.assertEqual(result, root)
        self.assertEqual(n2.next, n3)

        self.assertEqual(n4.next, n5)
        self.assertEqual(n5.next, n6)

        self.assertEqual(n7.next, n8)
        self.assertEqual(n8.next, n9)
        self.assertEqual(n9.next, n10)

    def test_2(self):
        n11 = Node()

        n7 = Node()
        n8 = Node(right=n11)
        n9 = Node()
        n10 = Node()

        n3 = Node(right=n7)
        n4 = Node(left=n8)
        n5 = Node(right=n9)
        n6 = Node(left=n10)

        n2 = Node(left=n3, right=n4)
        n3 = Node(left=n5, right=n6)

        root = Node(left=n2, right=n3)
        result = connect(root)

        self.assertEqual(result, root)
        self.assertEqual(n9.next, n10)


if __name__ == "__main__":
    unittest.main()
