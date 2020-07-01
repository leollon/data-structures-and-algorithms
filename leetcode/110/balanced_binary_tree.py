#!/usr/bin/env python3
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        return self._traverse(root)

    def _traverse(self, root):
        if not root:
            return True
        left_height = self._get_depth(root.left)
        right_height = self._get_depth(root.right)
        return self._traverse(root.left) and self._traverse(root.right) and \
            abs(left_height - right_height) <= 1

    def _get_depth(self, root):
        if not root:
            return 0
        # if root.left:
        #     return self._get_depth(root.left)
        # return self._get_depth(root.right)
        # We must get the max depth of left or right subtree
        return max(self._get_depth(root.left), self._get_depth(root.right)) + 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_isBalanced(self):

        array = [3, 9, 20, None, None, 15, 7]
        root = self.build_binary_tree(array)
        self.assertTrue(self.solution.isBalanced(root))

        array = [1, 2, 2, 3, 3, None, None, 4, 4]
        root = self.build_binary_tree(array)
        self.assertFalse(self.solution.isBalanced(root))

        array = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
        root = self.build_binary_tree(array)
        self.assertFalse(self.solution.isBalanced(root))

        array = [2, 1, 4, None, None, 3, 5, None, None, None, 6]
        root = self.build_binary_tree(array)
        self.assertFalse(self.solution.isBalanced(root))

    def build_binary_tree(self, array):

        root = TreeNode(array[0])
        node_list = [root]
        array_index, node_index, length = 1, 0, len(array)

        while array_index < length:

            val = array[array_index]
            curr_node = node_list[node_index]

            if val:
                curr_node.left = TreeNode(val)
                node_list.append(curr_node.left)

            array_index += 1

            if array_index >= length:
                break

            val = array[array_index]
            if val:
                curr_node.right = TreeNode(val)
                node_list.append(curr_node.right)

            array_index += 1
            node_index += 1

        return root


if __name__ == "__main__":
    unittest.main()

