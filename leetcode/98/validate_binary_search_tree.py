#!/usr/bin/env python3
"""

"""
import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RecursiveSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = [True]
        pointer: List[int] = []

        self._inorder(root, result, pointer)
        return result[0]

    def _inorder(self, root: TreeNode, result: List, pointer: List) -> None:
        if not root:
            return
        if result[0]:
            self._inorder(root.left, result, pointer)
            if not pointer:
                pointer.append(root.val)

            elif pointer[0] < root.val:
                pointer[0] = root.val
            else:
                result[0] = False
            self._inorder(root.right, result, pointer)
        return


class IterativeSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        is_valid = True
        results = []
        curr_node = root
        parent_nodes: List[TreeNode] = []

        while curr_node or parent_nodes:
            if curr_node and curr_node.left:
                parent_nodes.append(curr_node)
                curr_node = curr_node.left
                continue
            if curr_node:
                # 已经到达该子树最左边的结点或着不存在左子树
                results.append(curr_node.val)
            if parent_nodes and not curr_node:
                curr_node = parent_nodes.pop()
                results.append(curr_node.val)
            curr_node = curr_node.right

        for i in range(1, len(results)):
            is_valid = results[i] > results[i - 1]
            if not is_valid:
                break
        return is_valid


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.r_solution = RecursiveSolution()
        self.i_solution = IterativeSolution()

    def _build_binary_tree(self, array):

        node_index, array_index, length = 0, 1, len(array)
        root = TreeNode(array[0])
        node_list = [root]

        while array_index < length:

            curr_node = node_list[node_index]
            val = array[array_index]
            if val:
                curr_node.left = TreeNode(val)
                node_list.append(curr_node.left)
            array_index += 1

            if array_index == length:
                break

            val = array[array_index]
            if val:
                curr_node.right = TreeNode(val)
                node_list.append(curr_node.right)

            array_index += 1
            node_index += 1
        return root

    def test_isValidBST(self):

        array = [2, 1, 3]
        root = self._build_binary_tree(array)
        self.assertEqual(
            self.r_solution.isValidBST(root),
            self.i_solution.isValidBST(root))

        array = [1, 1]
        root = self._build_binary_tree(array)
        self.assertEqual(
            self.r_solution.isValidBST(root),
            self.i_solution.isValidBST(root))

        array = [1, None, 1]
        root = self._build_binary_tree(array)
        self.assertEqual(
            self.r_solution.isValidBST(root),
            self.i_solution.isValidBST(root))

        array = [3, None, 30, 10, None, None, 15, None, 45]
        root = self._build_binary_tree(array)
        self.assertEqual(
            self.r_solution.isValidBST(root),
            self.i_solution.isValidBST(root))

        array = [10, 5, 15, None, None, 6, 20]
        root = self._build_binary_tree(array)
        self.assertEqual(
            self.r_solution.isValidBST(root),
            self.i_solution.isValidBST(root))


if __name__ == "__main__":
    unittest.main()

