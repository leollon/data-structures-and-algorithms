"""Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its minimum depth = 2.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_depth = [-1]
        if not root:
            return 0
        self._helper(root, min_depth, 0)
        return min_depth[0]

    def _helper(self, node, min_depth, depth):
        depth += 1
        if not node:
            return
        if not node.left and not node.right:
            if min_depth[0] == -1:
                min_depth[0] = depth
            elif depth < min_depth[0]:
                min_depth[0] = depth
            return
        self._helper(node.left, min_depth, depth)
        self._helper(node.right, min_depth, depth)
