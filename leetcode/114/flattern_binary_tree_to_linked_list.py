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

        while curr_node or nodes_stack:
            if curr_node and curr_node.left:
                nodes_stack.append(curr_node.right)
                curr_node.right = curr_node.left
                curr_node.left = None
                curr_node = curr_node.right
            if curr_node and curr_node.right:
                curr_node = curr_node.right
                continue
            else:
                curr_node.right = nodes_stack.pop()
                curr_node = curr_node.right


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def _create_binary_tree(self, array: List[int]):
        array_index, node_index = 1, 0
        node_list = [TreeNode(array[0])]
        curr_node = node_list[node_index]
        root = node_list[node_index]
        length = len(array)

        while array_index < length:
            val = array[array_index]
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

    def test_flatten(self):

        array = [1, 2, 5, 3, 4, None, 6]

        array = [1, 2, None, 3, 4, None, None, None, 5, None, 6]


