"""Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        """
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[root.val]]
        self._helper(root, result, 0)
        return result

    def _helper(self, node, result, level):
        level += 1
        if not node:
            return
        if node.left:
            if len(result) <= level:
                result.append([])
            result[level].append(node.left.val)
        self._helper(node.left, result, level)
        if node.right:
            if len(result) <= level:
                result.append([])
            result[level].append(node.right.val)
        self._helper(node.right, result, level)
