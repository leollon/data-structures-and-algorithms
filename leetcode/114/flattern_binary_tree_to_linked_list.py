#!/usr/bin/env python3

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6

The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr_node = root
        nodes_stack: List[TreeNode] = []
        prev_node = root
        while curr_node or nodes_stack:
            if curr_node and curr_node.left:
                if curr_node.right:
                    nodes_stack.append(curr_node.right)
                curr_node.right = curr_node.left
                curr_node.left = None
                curr_node = curr_node.right
                prev_node = curr_node
                continue
            if curr_node and curr_node.right:
                curr_node = curr_node.right
                prev_node = curr_node
            elif not curr_node:
                curr_node = nodes_stack.pop()
                prev_node.right = curr_node
            elif not curr_node.right and nodes_stack:
                curr_node.right = nodes_stack.pop()
                curr_node = curr_node.right
            else:
                curr_node = None


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def _create_binary_tree(self, array: List[int]):
        array_index, node_index = 1, 0
        node_list = [TreeNode(array[0])]
        root = node_list[node_index]
        length = len(array)

        while array_index < length:
            val = array[array_index]
            curr_node = node_list[node_index]
            node_index += 1

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

        return root

    def _tree_to_string(self, root):
        result = ''
        current = root
        while current:
            result += str(current.val)
            if current.right:
                result += ", None, "
            current = current.right

        return result

    def test_flatten(self):

        array = [1, 2, 5, 3, 4, None, 6]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
            '1, None, 2, None, 3, None, 4, None, 5, None, 6',
            self._tree_to_string(root)
        )

        array = [1, 2, None, 3, 4, None, None, None, 5, None, 6]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
            '1, None, 2, None, 3, None, 4, None, 5, None, 6',
            self._tree_to_string(root)
        )

        array = [5, 4, None, 2, None, 1, 3]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
            '5, None, 4, None, 2, None, 1, None, 3',
            self._tree_to_string(root)
        )

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
           '1, None, 2, None, 4, None, 8, None, 9, None, 5, None, 10, None, 11, None, 3, None, 6, None, 12, None, 13, None, 7, None, 14, None, 15',
            self._tree_to_string(root)
        )

        array = [1, None, 2, None, 3, None, 4, None, 5]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
            '1, None, 2, None, 3, None, 4, None, 5',
            self._tree_to_string(root)
        )

        array = [1, 2, None, 3, None, 4, None, 5, None, 6]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
            '1, None, 2, None, 3, None, 4, None, 5, None, 6',
            self._tree_to_string(root)
        )

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        root = self._create_binary_tree(array)
        self.solution.flatten(root)
        self.assertEqual(
            '1, None, 2, None, 4, None, 8, None, 9, None, 5, None, 10, None, 3, None, 6, None, 7',
            self._tree_to_string(root)
        )


if __name__ == "__main__":
    unittest.main()
