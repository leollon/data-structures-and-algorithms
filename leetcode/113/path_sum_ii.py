"""Path total II
Given a binary tree and a total, find all root-to-leaf paths where each path's
total equals the given total.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and total = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, total: int):
        """
        :rtype: List[List[int]]
        """
        result = []
        self._helper(root, total, result, [])
        return result

    def _helper(self, node, total, result, sub):
        if not node:
            return
        sub.append(node.val)
        if not node.left and not node.right and total == node.val:
            result.append(sub[:])
            sub.pop()
            return
        self._helper(node.left, total - node.val, result, sub)
        self._helper(node.right, total - node.val, result, sub)
        sub.pop()
