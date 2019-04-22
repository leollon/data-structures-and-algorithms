import unittest
import random


from sum_root_to_leaf_numbers import TreeNode, Solution


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_binary_tree(array):
        if not array:
            return None
        root = TreeNode(array.pop(0))
        node_queue = [root]
        front = index = 0
        arr_len = len(array)
        while index < arr_len:
            node = node_queue[front]
            front += 1
            item = array[index]
            index += 1
            if item is not None:
                node.left = TreeNode(item)
                node_queue.append(node.left)

            if index >= arr_len:
                break

            item = array[index]
            index += 1
            if item is not None:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    def test_sumNumbers(self):
        s = Solution()

        array = [1, 2, 3]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.sumNumbers(tree), 25)

        array = [4, 9, 0, 5, 1]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.sumNumbers(tree), 1026)

        array = [1, None, 5]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.sumNumbers(tree), 15)

        array = [1, 2, 3, None, 2, 4, None, 5, 6]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.sumNumbers(tree), 2585)

        array = []
        tree = self.create_binary_tree(array)
        self.assertEqual(s.sumNumbers(tree), 0)

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.sumNumbers(tree), 10532)


if __name__ == "__main__":
    unittest.main()
