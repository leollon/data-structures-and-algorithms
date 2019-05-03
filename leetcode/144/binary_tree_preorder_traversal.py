"""Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionWithRecursion:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._helper(root, result)
        return result

    def _helper(self, node, result):
        if not node:
            return
        result.append(node.val)
        self._helper(node.left, result)
        self._helper(node.right, result)


class SolutionWithIteration:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        right_node = []
        node = root
        while node or right_node:
            result.append(node.val)
            if node.right:
                # 保存当前结点的右结点
                right_node.append(node.right)
            if node.left:
                # 遍历左结点
                node = node.left
                continue
            # 无左结点或到达叶子结点之后了
            if right_node:
                # 遍历完了左结点，得遍历右结点或者右子树（当存在左子树和右子树的时候）
                node = right_node.pop()
            else:
                # 无左子树的时候
                node = node.right
        return result
