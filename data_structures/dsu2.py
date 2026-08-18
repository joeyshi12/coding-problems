import unittest


class DisjointSetUnion:
    """Disjoint set union implementation with a dictionary"""

    def __init__(self):
        self.parents = {}

    def find(self, key: str):
        if key not in self.parents:
            return key
        self.parents[key] = self.find(self.parents[key])
        return self.parents[key]
    
    def union(self, key1: str, key2: str):
        root1 = self.find(key1)
        root2 = self.find(key2)
        if root1 == root2:
            return
        self.parents[root1] = root2


class TestDisjointSetUnion(unittest.TestCase):
    def test_union(self):
        dsu = DisjointSetUnion()
        dsu.union("a", "b")
        dsu.union("c", "a")
        dsu.union("a", "d")
        keys = list("abcd")
        self.assertListEqual([dsu.find(key) for key in keys], ["d", "d", "d", "d"])
