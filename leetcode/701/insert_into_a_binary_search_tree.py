#!/usr/bin/env python3
"""
Given the root node of a binary search tree (BST) and a value to be inserted
into the tree, insert the value into the BST. Return the root node of the BST
after the insertion. It is guaranteed that the new value does not exist in the
original BST.

Note that there may exist multiple valid ways for the insertion, as long as the
tree remains a BST after insertion. You can return any of them.

For example,

    Given the tree:
            4
           / \
          2   7
         / \
        1   3
    And the value to insert: 5
    You can return this binary search tree:

             4
           /   \
          2     7
         / \   /
        1   3 5
    This tree is also valid:

             5
           /   \
          2     7
         / \
        1   3
             \
              4

Constraints:

    - The number of nodes in the given tree will be between 0 and 10^4.
    - Each node will have a unique integer value from 0 to -10^8, inclusive.
    - -10^8 <= val <= 10^8
    - It's guaranteed that val does not exist in the original BST.
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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def helper(root, prev_root, val):
            if not root:
                new_node = TreeNode(val)
                if prev_root.val > val:
                    new_node.left = prev_root.left
                    prev_root.left = new_node
                else:
                    new_node.right = prev_root.right
                    prev_root.right = new_node
                return

            if val > root.val:
                helper(root.right, root, val)
            else:
                helper(root.left, root, val)

        if root:
            helper(root, root, val)
            return root
        return TreeNode(val)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def _create_BST(self, array: List[int]) -> TreeNode:
        if not array:
            return None
        node_index, array_index = 0, 1
        node_list = [TreeNode(array[0])]
        root = node_list[node_index]
        length = len(array)

        while array_index < length:
            curr_node = node_list[node_index]
            node_index += 1

            val = array[array_index]
            array_index += 1

            if val:
                curr_node.left = TreeNode(val)
                node_list.append(curr_node.left)

            if array_index == length:
                break

            val = array[array_index]
            array_index += 1

            if val:
                curr_node.right = TreeNode(val)
                node_list.append(curr_node.right)

        return root

    def _inorder(self, root: TreeNode) -> List[int]:
        curr_node = root
        results = []
        node_stack: List[TreeNode] = []

        while curr_node or node_stack:
            if curr_node and curr_node.left:
                node_stack.append(curr_node)
                curr_node = curr_node.left
                continue
            if curr_node:
                results.append(curr_node.val)

            if not curr_node and node_stack:
                curr_node = node_stack.pop()
                results.append(curr_node.val)
            curr_node = curr_node.right
        return results

    def test_insertIntoBST(self):
        array = [4, 2, 7, 1, 3]
        val = 5
        root = self._create_BST(array)
        self.solution.insertIntoBST(root, val)
        self.assertEqual([1, 2, 3, 4, 5, 7], self._inorder(root))

        array = [4, 2, 7, 1, 3]
        val = 0
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([0, 1, 2, 3, 4, 7], self._inorder(root))

        array = [4, 2, 7, 1, 3]
        val = 8
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([1, 2, 3, 4, 7, 8], self._inorder(root))

        array = [4, 2, 7, 1, 3]
        val = 6
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([1, 2, 3, 4, 6, 7], self._inorder(root))

        array = []
        val = 1
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([1], self._inorder(root))

        array = [1]
        val = 2
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([1, 2], self._inorder(root))

        array = [10, 4, 15, 2, 5, 12, 18]
        val = 1
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([1, 2, 4, 5, 10, 12, 15, 18], self._inorder(root))

        array = [10, 4, 15, 2, 5, None, 18]
        val = 12
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([2, 4, 5, 10, 12, 15, 18], self._inorder(root))

        array = [10, 4, 15, 2, 5, 12]
        val = 16
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([2, 4, 5, 10, 12, 15, 16], self._inorder(root))

        array = [10, 4, 15, 2, None, 12, 18]
        val = 5
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([2, 4, 5, 10, 12, 15, 18], self._inorder(root))

        array = [10, 3, 15, 2, None, 12, 18]
        val = 4
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([2, 3, 4, 10, 12, 15, 18], self._inorder(root))

        array = [10, 3, 15, 2, None, 12, 18]
        val = 1
        tree = self._create_BST(array)
        root = self.solution.insertIntoBST(tree, val)
        self.assertEqual([1, 2, 3, 10, 12, 15, 18], self._inorder(root))


if __name__ == "__main__":
    unittest.main()
