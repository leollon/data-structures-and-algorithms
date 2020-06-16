

import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
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


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.build = Solution()

    def test_build_bst(self):

        preorder = [7, 20, 19, 12]
        root = self.build.bstFromPreorder(preorder)
        preorder.insert(0, 7)
        result = []
        self.pre_order_visit(root, result)
        self.assertEqual(preorder, result)

        preorder = [8, 5, 1, 7, 10, 12]
        root = self.build.bstFromPreorder(preorder)
        preorder.insert(0, 8)
        result = []
        self.pre_order_visit(root, result)
        self.assertEqual(preorder, result)

        preorder = [1, 2, 3, 4, 5, 6, 7, 8]
        root = self.build.bstFromPreorder(preorder)
        preorder.insert(0, 1)
        result = []
        self.pre_order_visit(root, result)
        self.assertEqual(preorder, result)

        preorder = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        root = self.build.bstFromPreorder(preorder)
        preorder.insert(0, 9)
        result = []
        self.pre_order_visit(root, result)
        self.assertEqual(preorder, result)

        preorder = [8, 7, 1, 10, 12, 15]
        root = self.build.bstFromPreorder(preorder)
        preorder.insert(0, 8)
        result = []
        self.pre_order_visit(root, result)
        self.assertEqual(preorder, result)

    def pre_order_visit(self, root: TreeNode, result: List[int]) -> None:

        if not root:
            return
        result.append(root.val)
        self.pre_order_visit(root.left, result)
        self.pre_order_visit(root.right, result)


if __name__ == "__main__":
    unittest.main()

