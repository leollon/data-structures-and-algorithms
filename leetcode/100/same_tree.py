"""

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        if not p.right and not p.left and not q.right and not q.left:
            if p.val == q.val:
                return True
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def build_tree(self, array: List[int]) -> TreeNode:
        length = len(array)

        if not length:
            return None

        array_index, node_index = 1, 0
        node_list = []
        root = TreeNode(array[array_index - 1])
        node_list.append(root)

        while array_index < length:

            curr_node = node_list[node_index]
            val = array[array_index]

            if val:
                new_node = TreeNode(val)
                curr_node.left = new_node
                node_list.append(curr_node)

            array_index += 1

            if array_index >= length:
                break

            val = array[array_index]

            if val:
                new_node = TreeNode(val)
                curr_node.right = new_node
                node_list.append(curr_node)

            array_index += 1
            node_index += 1

        return root

    def test_isSameTree(self):

        array1, array2 = [], []
        tree1, tree2 = self.build_tree(array1), self.build_tree(array2)
        self.assertEqual(True, self.solution.isSameTree(tree1, tree2))

        array1, array2 = [1, 2, 3], [1, 2, 3]
        tree1, tree2 = self.build_tree(array1), self.build_tree(array2)
        self.assertEqual(True, self.solution.isSameTree(tree1, tree2))

        array1, array2 = [1, 1, 2], [1, 1, 2]
        tree1, tree2 = self.build_tree(array1), self.build_tree(array2)
        self.assertEqual(True, self.solution.isSameTree(tree1, tree2))

        array1, array2 = [1], []
        tree1, tree2 = self.build_tree(array1), self.build_tree(array2)
        self.assertEqual(False, self.solution.isSameTree(tree1, tree2))

        array1, array2 = [1, 1, 2], [1, 2, 1]
        tree1, tree2 = self.build_tree(array1), self.build_tree(array2)
        self.assertEqual(False, self.solution.isSameTree(tree1, tree2))

        array1, array2 = [1, 2], [1, None, 2]
        tree1, tree2 = self.build_tree(array1), self.build_tree(array2)
        self.assertEqual(False, self.solution.isSameTree(tree1, tree2))


if __name__ == "__main__":
    unittest.main()

