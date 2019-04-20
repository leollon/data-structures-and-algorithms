"""Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return True, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self._helper(root, sum)

    def _helper(self, node, sum):
        if not node:
            return False
        if not node.left and not node.right and sum == node.val:
            return True
        return self._helper(node.left, sum - node.val) or self._helper(node.right, sum - node.val)
