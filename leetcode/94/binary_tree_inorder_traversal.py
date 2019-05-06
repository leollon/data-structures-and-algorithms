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
        subtrees_root = []
        while node or subtrees_root:
            if node and node.left:
                # 访问当前结点左结点，将该当前结点该左结点所在的子树的根结点，并将这个
                # 根结点放入子树根列表中
                subtrees_root.append(node)
                node = node.left
                continue
            if node:
                # 已经到达该子树最左边的结点或不存在左子树
                result.append(node.val)
            if not node and subtrees_root:
                # 到达叶子结点之后，子树的根结点出栈，并取该根结点的值放入要返回的结果中
                node = subtrees_root.pop()
                result.append(node.val)
            node = node.right  # 访问当前结点的右子树或叶子结点
        return result
