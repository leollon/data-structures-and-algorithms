"""Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

    Input:

       1
     /   \
    2     3
     \
      5

    Output: ["1->2->5", "1->3"]
    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        """
        :rtype: List[str]
        """
        result = []
        self._helper(root, '', result)
        return result

    def _helper(self, node, s, result):
        if not node:
            return
        if node and not node.left and not node.right:
            result.append(s + str(node.val))
            return
        s += str(node.val)
        self._helper(node.left, s + '->', result)   # 当前结点的左孩子结点
        self._helper(node.right, s + '->', result)  # 当前结点的右孩子结点
