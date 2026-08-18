import unittest


class DisjointSetUnion:
    """Disjoint set union implementation with a fixed array of ints"""

    def __init__(self, size: int):
        self.parents = [-1] * size

    def find(self, key: int):
        if self.parents[key] == -1:
            return key
        self.parents[key] = self.find(self.parents[key])
        return self.parents[key]
    
    def union(self, key1: int, key2: int):
        root1 = self.find(key1)
        root2 = self.find(key2)
        if root1 == root2:
            return
        self.parents[root1] = root2


class TestDisjointSetUnion(unittest.TestCase):
    def test_union(self):
        dsu = DisjointSetUnion(10)
        dsu.union(0, 2)
        dsu.union(4, 2)
        dsu.union(0, 6)
        self.assertListEqual([dsu.find(i) for i in range(10)], [6, 1, 6, 3, 6, 5, 6, 7, 8, 9])
        self.assertListEqual(dsu.parents, [6, -1, 6, -1, 6, -1, -1, -1, -1, -1])
