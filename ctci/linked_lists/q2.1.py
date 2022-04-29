import unittest

class Node:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next_node = next_node

def remove_dups(head: Node) -> Node:
    # Time complexity: O(n^2)
    # this can be improved by keeping track of visited
    curr = head
    while curr:
        remove(curr.val, curr)
        curr = curr.next_node
    return head

def remove(val: int, head: Node) -> None:
    if not head:
        return
    curr = head
    while curr.next_node:
        next_node = curr.next_node
        if next_node and next_node.val == val:
            curr.next_node = next_node.next_node
        curr = next_node

class TestRemoveDups(unittest.TestCase):
    # TODO: add more tests

    def test_null(self):
        result = remove_dups(None)
        self.assertLinkedListEqual(result, None)

    def test_singleton_list(self):
        head = Node(0)
        result = remove_dups(head)
        self.assertLinkedListEqual(result, Node(0))

    def test_same_elements(self):
        head = Node(0, Node(0, Node(0)))
        result = remove_dups(head)
        self.assertLinkedListEqual(result, Node(0))

    def test_non_trivial(self):
        head = Node(0, Node(1, Node(0)))
        result = remove_dups(head)
        self.assertLinkedListEqual(result, Node(0, Node(1)))

    def assertLinkedListEqual(self, l1: Node, l2: Node):
        while l1 and l2:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next_node
            l2 = l2.next_node
        self.assertIsNone(l1)
        self.assertIsNone(l2)

if __name__ == "__main__":
    unittest.main()
