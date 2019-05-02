"""Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

        1
       / \
      2   2
       \   \
       3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left = []
        self._from_left(root, left)  # start from left subtree at first
        right = []
        self._from_right(root, right)  # start from right subtree at first
        return left == right

    def _from_left(self, node, result):
        if node:
            result.append(node.val)
        if not node:
            result.append(node)
            return
        self._from_left(node.left, result)
        self._from_left(node.right, result)

    def _from_right(self, node, result):
        if node:
            result.append(node.val)
        if not node:
            result.append(node)
            return
        self._from_right(node.right, result)
        self._from_right(node.left, result)
