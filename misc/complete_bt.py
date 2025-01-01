"""
Given a binary tree, determine if it is complete.
def. A complete binary tree is a binary tree, such that all nodes except for the last level have exactly 2 children.
"""

from typing import Optional


class BinaryTree:
    def __init__(self, data: int, left: Optional["BinaryTree"] = None, right: Optional["BinaryTree"] = None):
        self.data = data
        self.left = left
        self.right = right

    def is_complete(self) -> bool:
        children: list[BinaryTree] = [self]
        curr_length: int = 1
        while children:
            next_children: list[BinaryTree] = []
            for child in children:
                if child.left is not None:
                    next_children.append(child.left)
                if child.right is not None:
                    next_children.append(child.right)

            if len(children) != curr_length and len(next_children) > 0:
                return False

            children = next_children
            curr_length *= 2

        return True

tree1 = BinaryTree(1, BinaryTree(0), BinaryTree(2))
assert tree1.is_complete()

tree2 = BinaryTree(1, None, BinaryTree(2))
assert tree2.is_complete()

tree3 = BinaryTree(1, BinaryTree(0))
assert tree3.is_complete()

tree4 = BinaryTree(2, BinaryTree(0, None, BinaryTree(1)))
assert not tree4.is_complete()
