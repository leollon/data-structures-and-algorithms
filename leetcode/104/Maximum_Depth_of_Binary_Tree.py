"""Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        depth = 0
        max_depth = [1]
        self.helper(root, max_depth, depth)
        return max_depth[0]
    
    def helper(self, node, max_depth, depth):
        if not node:
            if depth > max_depth[0]:
                max_depth[0] = depth
                return
        else:
            self.helper(node.left, max_depth, depth + 1) # 遍历当前结点的左子树
            self.helper(node.right, max_depth, depth + 1) # 遍历当前结点右子树结点
