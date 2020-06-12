"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

    > Google: 90% of our engineers use the software you wrote (Homebrew),
    > but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionWithRecursion:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self._helper(root)
        return root

    def _helper(self, node: TreeNode):
        if not node:
            return
        node.left, node.right = node.right, node.left
        if node.left:
            self._helper(node.left)
        if node.right:
            self._helper(node.right)
