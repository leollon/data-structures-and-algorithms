"""Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]
    Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNone
        :rtype: List[int]
        """
        result = []
        self._helper(root, result, 0)
        return result

    def _helper(self, node, result, level):
        if not node:
            return
        level += 1
        if len(result) < level:
            result.append(node.val)
        self._helper(node.right, result, level)
        self._helper(node.left, result, level)
