from collections import deque
import unittest

class Node:
    def __init__(self, name, neighbours=None):
        self.name = name
        self.neighbours = neighbours if neighbours else []

def route_exists(u: Node, v: Node) -> bool:
    # TODO: optimize with bidirectional search
    if u is None or v is None:
        return False
    return path_to_target_exists(u, v.name) \
        or path_to_target_exists(v, u.name)

def path_to_target_exists(u, target):
    if u is None:
        return False
    visited = set()
    queue = deque()
    visited.add(u.name)
    queue.append(u)
    while queue:
        p = queue.popleft()
        for node in p.neighbours:
            if node.name == target:
                return True
            if node.name not in visited:
                visited.add(node.name)
                queue.append(node)
    return False

class TestRouteExists(unittest.TestCase):
    def test_null(self):
        result = route_exists(None, None)
        self.assertFalse(result)

    def test_null_source(self):
        A = Node("A")
        result = route_exists(A, None)
        self.assertFalse(result)

    def test_null_destination(self):
        A = Node("A")
        result = route_exists(None, A)
        self.assertFalse(result)

    def test_isolated_nodes(self):
        """A    B"""
        A = Node("A")
        B = Node("B")
        result = route_exists(A, B)
        self.assertFalse(result)

    def test_adjacent_route_exists(self):
        """A -> B"""
        A = Node("A")
        B = Node("B")
        A.neighbours.append(B)
        result = route_exists(A, B)
        self.assertTrue(result)

    def test_non_adjacent_route_exists(self):
        """A -> B -> C"""
        A = Node("A")
        B = Node("B")
        C = Node("C")
        A.neighbours.append(B)
        B.neighbours.append(C)
        result = route_exists(A, C)
        self.assertTrue(result)

    def test_non_adjacent_route_does_not_exist(self):
        """A -> B <- C"""
        A = Node("A")
        B = Node("B")
        C = Node("C")
        A.neighbours.append(B)
        C.neighbours.append(B)
        result = route_exists(A, C)
        self.assertFalse(result)

    def test_cycle_route_exists(self):
        """
        A -> B
        ^    |
        |    v
        D <- C
        """
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        A.neighbours.append(B)
        B.neighbours.append(C)
        C.neighbours.append(D)
        D.neighbours.append(A)
        result = route_exists(A, A)
        self.assertTrue(result)

    def test_isolated_components_route_does_not_exist(self):
        """
        A -> B
        |
        v
        C -> D

        E -> F -> G -> E
        """
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")
        F = Node("F")
        G = Node("G")
        A.neighbours.append(B)
        A.neighbours.append(C)
        C.neighbours.append(D)
        E.neighbours.append(F)
        F.neighbours.append(G)
        G.neighbours.append(E)
        result = route_exists(A, E)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
