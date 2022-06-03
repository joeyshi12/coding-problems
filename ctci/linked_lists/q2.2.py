from typing import List
import unittest


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def kth_to_last(head: Node, k: int) -> Node:
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next_node
    return nodes[-k]


def to_linked_list(nums: List[int]):
    head = Node(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next_node = Node(nums[i])
        curr = curr.next_node
    return head


class TestKthToLast(unittest.TestCase):
    TEST_DATA = [
        (([0], 1), 0),
        (([0, 1, 2], 1), 2),
        (([2, 7, 1, 8], 3), 7),
        (([3, 1, 4, 2, 5], 5), 3),
    ]

    def test_kth_to_last(self):
        for (nums, k), expected in self.TEST_DATA:
            head = to_linked_list(nums)
            result = kth_to_last(head, k).data
            print(f"{nums, k} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
