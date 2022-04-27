from collections import deque
import unittest

class BTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LLNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

def create_depth_list(root: BTNode):
    # TODO: implement
    if root is None:
        return root

    queue = deque()
    visited = set()
    queue.append(root)
    visited.add(root)

    curr_head = LLNode(root.val)
    level = 0
    remaining = 1

    while queue:
        p = queue.popleft()

        if p.left and p.left not in visited:
            visited.add(p.left)
            queue.append(p.left)

        if p.right and p.right not in visited:
            visited.add(p.right)
            queue.append(p.right)

    return None

class TestCreateDepthList(unittest.TestCase):
    def test_null(self):
        result = create_depth_list(None)
        self.assertEqual(result, None)
