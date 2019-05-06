"""Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionWithRecursion:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rypte: List[int]
        """
        result = []
        if not root:
            return result
        self._helper(root.left, result)  # 左子树
        self._helper(root.right, result)  # 右子树
        result.append(root.val)  # 根结点
        return result

    def _helper(self, node, result):
        if not node:
            return
        self._helper(node.left, result)
        self._helper(node.right, result)
        result.append(node.val)
