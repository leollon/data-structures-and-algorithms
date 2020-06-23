"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
    http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can
have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
        1
       / \
      2   3
     / \  /
    4  5 6

Output: 6

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
    def countNodes(self, root: TreeNode) -> int:
        result = [0]
        self._helper(root, result)
        return result[0]

    def _helper(self, root: TreeNode, result: List):
        if not root:
            return
        result[0] += 1
        self._helper(root.left, result)
        self._helper(root.right, result)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_countNodes(self):

        array = [1, 2, 3, None, 4, None, 5, 6, 7]
        root = self.build_complete_binary_tree(array)
        self.assertEqual(7, self.solution.countNodes(root))

        array = [1, 2, 3, 4, 5, 6]
        root = self.build_complete_binary_tree(array)
        self.assertEqual(6, self.solution.countNodes(root))

    def build_complete_binary_tree(self, array):
        node_list = []
        length = len(array)
        node_index, array_index = 0, 1
        root = TreeNode(array[array_index - 0])
        node_list.append(root)

        while array_index < length:
            val = array[array_index]
            curr_node = node_list[node_index]
            if val:
                new_node = TreeNode(val)
                curr_node.left = new_node
                node_list.append(curr_node.left)
            array_index += 1

            if array_index >= length:
                break

            val = array[array_index]
            if val:
                new_node = TreeNode(val)
                curr_node.right = new_node
                node_list.append(curr_node.right)
            array_index += 1
            node_index += 1

        return root


if __name__ == "__main__":
    unittest.main()

