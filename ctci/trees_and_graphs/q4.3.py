import unittest
from typing import List, Optional

class BTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LLNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

def create_depth_list(root: Optional[BTNode]) -> List[LLNode]:
    if root is None:
        return []

    depth_list = []
    level = [root]
    while len(level) > 0:
        depth_node = LLNode(level[0].val)
        curr_node = depth_node
        for i in range(1, len(level)):
            curr_node.next_node = LLNode(level[i].val)
            curr_node = curr_node.next_node

        depth_list.append(depth_node)

        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        level = next_level

    return depth_list


class TestCreateDepthList(unittest.TestCase):
    def test_null(self):
        depth_list = create_depth_list(None)
        self.assertListEqual(depth_list, [])

    def test_btree(self):
        btree = BTNode(1, BTNode(2, BTNode(4)), BTNode(3, right=BTNode(5)))
        depth_list = create_depth_list(btree)
        depth_values = []
        for depth_node in depth_list:
            values = []
            while depth_node is not None:
                values.append(depth_node.data)
                depth_node = depth_node.next_node
            depth_values.append(values)
        self.assertEqual(depth_values, [[1], [2, 3], [4, 5]])


if __name__ == "__main__":
    unittest.main()
