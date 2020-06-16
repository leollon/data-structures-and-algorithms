"""
Given the root node of a binary search tree (BST) and a value. You need to find
the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. If such node doesn't exist,
you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node
with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the
expected output (serialized tree format) as [], not null.
"""
import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.search = Solution()

    def test_search_bst_success(self):

        preorder = [7, 20, 19, 12]
        root = self._bstFromPreorder(preorder)
        node = self.search.searchBST(root, 19)
        self.assertTrue(node is not None and node.val == 19)

        preorder = [8, 5, 1, 7, 10, 12]
        root = self._bstFromPreorder(preorder)
        node = self.search.searchBST(root, 10)
        self.assertTrue(node is not None and node.val == 10)

        preorder = [1, 2, 3, 4, 5, 6, 7, 8]
        root = self._bstFromPreorder(preorder)
        node = self.search.searchBST(root, 5)
        self.assertTrue(node is not None and node.val == 5)

    def test_search_bst_none(self):

        preorder = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        root = self._bstFromPreorder(preorder)
        node = self.search.searchBST(root, 88)
        assert node is None

    def _bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        root = TreeNode(preorder.pop(0))
        for val in preorder:
            pre_curr_node = curr_node = root
            while curr_node:
                pre_curr_node = curr_node
                if val > curr_node.val:
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left
            curr_node = TreeNode(val)
            if pre_curr_node.val > val:
                pre_curr_node.left = curr_node
            else:
                pre_curr_node.right = curr_node

        return root


if __name__ == "__main__":
    unittest.main()

