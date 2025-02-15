# https://leetcode.com/problems/design-hashmap/

from typing import List
import unittest

class Node:
    def __init__(self, key, val, next_node=None):
        self.key = key
        self.val = val
        self.next_node = next_node

class HashMap:
    HASH_TABLE_SIZE: int = 16
    table: List[Node]

    def __init__(self):
        self.table = [None] * self.HASH_TABLE_SIZE

    def put(self, key: int, value: int) -> None:
        idx = key % self.HASH_TABLE_SIZE
        if not self.table[idx]:
            self.table[idx] = Node(key, value)
            return
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.val = value
                return
            if curr.next_node is None:
                curr.next_node = Node(key, value)
                return
            curr = curr.next_node

    def get(self, key: int) -> int:
        idx = key % self.HASH_TABLE_SIZE
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next_node
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.HASH_TABLE_SIZE
        curr = self.table[idx]
        if not curr:
            return
        if curr.key == key:
            self.table[idx] = curr.next_node
            return
        while curr.next_node:
            next_node = curr.next_node
            if next_node.key == key:
                curr.next_node = next_node.next_node
                return
            curr = next_node

class TestHashMap(unittest.TestCase):
    hashmap: HashMap

    def setUp(self):
        self.hashmap = HashMap()

    def test_put_single_update(self):
        key = 0
        self.hashmap.put(key, 1)
        val = self.hashmap.get(key)
        self.assertEqual(val, 1)

        self.hashmap.put(key, 3)
        val = self.hashmap.get(key)
        self.assertEqual(val, 3)

    def test_put_multiple(self):
        key1 = 0
        self.hashmap.put(key1, 3)
        val1 = self.hashmap.get(key1)

        key2 = HashMap.HASH_TABLE_SIZE - 1
        self.hashmap.put(key2, 2)
        val2 = self.hashmap.get(key2)

        key3 = (HashMap.HASH_TABLE_SIZE - 1) // 2
        self.hashmap.put(key3, 3)
        val3 = self.hashmap.get(key3)

        self.assertEqual(val1, 3)
        self.assertEqual(val2, 2)
        self.assertEqual(val3, 3)

    def test_put_collide(self):
        key1 = 0
        self.hashmap.put(key1, 1)
        val1 = self.hashmap.get(key1)

        key2 = HashMap.HASH_TABLE_SIZE
        self.hashmap.put(key2, 2)
        val1 = self.hashmap.get(key1)
        val2 = self.hashmap.get(key2)

        self.assertEqual(val1, 1)
        self.assertEqual(val2, 2)

    def test_get(self):
        key = 0
        val = self.hashmap.get(key)
        self.assertEqual(val, -1)

        self.hashmap.put(key, 2)
        val = self.hashmap.get(key)
        self.assertEqual(val, 2)

    def test_remove_empty(self):
        val = self.hashmap.get(0)
        self.assertEqual(val, -1)
        self.hashmap.remove(0)
        val = self.hashmap.get(0)
        self.assertEqual(val, -1)

    def test_remove_head(self):
        self.hashmap.put(0, 1)
        self.hashmap.put(HashMap.HASH_TABLE_SIZE, 2)
        self.hashmap.remove(0)
        val1 = self.hashmap.get(0)
        val2 = self.hashmap.get(HashMap.HASH_TABLE_SIZE)
        self.assertEqual(val1, -1)
        self.assertEqual(val2, 2)

    def test_remove_tail(self):
        self.hashmap.put(0, 1)
        self.hashmap.put(HashMap.HASH_TABLE_SIZE, 2)
        self.hashmap.remove(HashMap.HASH_TABLE_SIZE)
        val1 = self.hashmap.get(0)
        val2 = self.hashmap.get(HashMap.HASH_TABLE_SIZE)
        self.assertEqual(val1, 1)
        self.assertEqual(val2, -1)

if __name__ == "__main__":
    unittest.main()
