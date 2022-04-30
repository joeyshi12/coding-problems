# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import List, Optional
import unittest

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    while is_duplicate(head):
        head = find_next_unique(head)
    curr = head
    while curr:
        while is_duplicate(curr.next_node):
            curr.next_node = find_next_unique(curr.next_node)
        curr = curr.next_node
    return head

def find_next_unique(node: Optional[ListNode]) -> Optional[ListNode]:
    if not node:
        return node
    next_node = node.next_node
    while next_node and next_node.val == node.val:
        next_node = next_node.next_node
    return next_node

def is_duplicate(node: Optional[ListNode]) -> Optional[ListNode]:
    if not node:
        return False
    next_node = node.next_node
    return next_node and next_node.val == node.val

def convert_to_linked_list(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for val in nums[1:]:
        curr.next_node = ListNode(val)
        curr = curr.next_node
    return head

class TestDeleteDuplicates(unittest.TestCase):
    TEST_DATA = [
        ([], []),
        ([1], [1]),
        ([1, 1], []),
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
    ]

    def test_delete_duplicates(self):
        for nums, expected_nums in self.TEST_DATA:
            head = convert_to_linked_list(nums)
            curr1 = delete_duplicates(head)
            curr2 = convert_to_linked_list(expected_nums)
            while curr1 and curr2:
                self.assertEqual(curr1.val, curr2.val)
                curr1 = curr1.next_node
                curr2 = curr2.next_node
            self.assertIsNone(curr1)
            self.assertIsNone(curr2)
            print(f"{nums} -> {expected_nums}")

if __name__ == "__main__":
    unittest.main()
