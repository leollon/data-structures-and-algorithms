"""Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

        1
       / \
      2   2
       \   \
       3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionWithRecursion:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            # not a tree
            return True
        return self._helper(root.left, root.right)

    def _helper(self, left, right):
        if not left and not right:
            # reach the leaf node
            return True
        if not left and right:
            # the height of left subtree is less than the right one
            return False
        elif left and not right:
            # the height of left subtree is greater than the right one
            return False
        return left.val == right.val and self._helper(left.left, right.right) \
            and self._helper(left.right, right.left)
