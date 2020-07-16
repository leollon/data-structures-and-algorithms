#!/usr/bin/env python3
"""
Given an integer array with no duplicates. A maximum tree building on this
array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray
divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray
divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this
tree.

Example 1:
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the following tree:

          6
        /   \
       3     5
        \    /
         2  0
           \
            1
Note:
    1. The size of the given array will be in the range [1,1000].
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        max_value = max(nums)
        max_value_index = nums.index(max_value)
        left, right = nums[:max_value_index], nums[max_value_index+1:]
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _traversal(self, root):
        queue: List[TreeNode] = [root]
        results = []

        while queue:
            curr_node = queue.pop(0)
            if not curr_node:
                if queue:
                    # do not append None when there is no right leaf at the
                    # bottom of the binary tree
                    results.append(curr_node)
                continue
            results.append(curr_node.val)
            if curr_node.left or curr_node.right:
                queue.append(curr_node.left)
                queue.append(curr_node.right)
        return results

    def test_constructMaximumBinaryTree(self):
        array: List[int] = [3, 2, 1, 6, 0, 5]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual(
            [6, 3, 5, None, 2, 0, None, None, 1], self._traversal(root))

        array: List[int] = [6, 5, 4, 3, 2, 1]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual(
            [6, None, 5, None, 4, None, 3, None, 2, None, 1],
            self._traversal(root))

        array: List[int] = [1, 2, 3, 4, 5, 6]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual(
            [6, 5, None, 4, None, 3, None, 2, None, 1], self._traversal(root))

        array: List[int] = [3, 2, 1, 6, 4, 5]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual(
            [6, 3, 5, None, 2, 4, None, None, 1], self._traversal(root))

        array: List[int] = [1]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual([1], self._traversal(root))

        array: List[int] = [1, 2]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual([2, 1], self._traversal(root))

        array: List[int] = [2, 1]
        root = self.solution.constructMaximumBinaryTree(array)
        self.assertEqual([2, None, 1], self._traversal(root))


if __name__ == "__main__":
    unittest.main()
