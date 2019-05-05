"""Binary Tree inorder traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionWithRecursion:
    def inorderTraversal(self, root):
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
        self._helper(node.left, result)
        result.append(node.val)
        self._helper(node.right, result)


class SolutionWithIteration:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        node = root
        mid_nodes = []
        while node or mid_nodes:
            if node and node.left:
                mid_nodes.append(node)
                node = node.left
                continue
            if node:
                # 已经到达该子树最左边的结点或着不存在左子树
                result.append(node.val)
            if node and node.right:
                node = node.right
                continue
            else:
                if mid_nodes:
                    node = mid_nodes.pop()
                    result.append(node.val)
            node = node.right
        return result
