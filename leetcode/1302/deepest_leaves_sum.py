"""Given a binary tree, return the sum of values of its deepest leaves.


Example 1:

    Input: root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    Output: 15


Constraints:

    -  The number of nodes in the tree is between 1 and 10^4.
    -  The value of nodes is between 1 and 100.
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

    def deepestLeavesSum(self, root: TreeNode) -> int:

        # index 0 store max depth, index 1 stores the sum of the deepest leaves
        results = [0, 0]
        self._compute_max_depth(root, results, 0)
        self._helper(root, 0, results)
        return results[1]

    def _compute_max_depth(self, root: TreeNode, results: List[int], curr_depth: int):
        if not root:
            return
        if not root.right and not root.left:
            if curr_depth > results[0]:
                results[0] = curr_depth
            return
        self._compute_max_depth(root.left, results, curr_depth + 1)
        self._compute_max_depth(root.right, results, curr_depth + 1)

    def _helper(self, root: TreeNode, curr_depth: int, results: List[int]):
        if not root:
            return
        if not root.right and not root.left:
            if curr_depth > results[0]:
                # compare curr_depth with max_depth
                results[0] = curr_depth
        self._helper(root.left, curr_depth + 1, results)
        self._helper(root.right, curr_depth + 1, results)

        if curr_depth == results[0]:
            # curr_depth is equivalent to max_depth
            results[1] += root.val


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_deepestLeavesSum(self):

        data = [1, 2, 3, 4, 5, 6, 7]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(22, result)

        data = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(15, result)

        data = [1, 2, 3, 4, 5, None, 6, 7]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(7, result)

        data = [1, 2, 3, 4, 5, None, 6, 7, None, 3, None, None, 8]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(18, result)

        data = [50, None, 54, 98, 6, None, None, None, 34]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(34, result)

        data = [20, 1, None, 23, 22, 17, 18]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(35, result)

        data = [20, 1, None, 23, 22, 17]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(17, result)

        data = [20, 1, None, 23, 22, None, 17]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(17, result)

        data = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, 9, 8]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(24, result)

        data = [1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, 9, 8]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(17, result)

        data = [1, 2, 3, 4, 5, None, 6, None, None, 7, None, None, None, 9, 8]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(17, result)

        data = [1]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(1, result)

        data = [12]
        root = self.build_binary_tree(data)
        result = self.solution.deepestLeavesSum(root)
        self.assertEqual(12, result)

    def build_binary_tree(self, data):
        node_list = [TreeNode(data[0])]
        root = node_list[0]
        node_index, data_index, length = 0, 1, len(data)

        while data_index < length:
            curr_node = node_list[node_index]

            # left child
            val = data[data_index]
            if val:
                new_node = TreeNode(val)
                node_list.append(new_node)
                curr_node.left = new_node
            data_index += 1

            if data_index == length:
                break

            # right child
            val = data[data_index]
            if val:
                new_node = TreeNode(val)
                node_list.append(new_node)
                curr_node.right = new_node
            data_index += 1
            node_index += 1

        return root


if __name__ == "__main__":
    unittest.main()

