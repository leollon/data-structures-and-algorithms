import unittest
from random import randint, choice, shuffle

from minimum_depth_of_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_binary_tree(array):
        if not array:
            return
        root = TreeNode(array.pop(0))
        node_queue = [root]
        front = 0
        length = len(array)
        while length:
            node = node_queue[front]
            front += 1
            item = array.pop(0)
            length -= 1
            if item is not None:
                node.left = TreeNode(item)
                node_queue.append(node.left)

            if length == 0:
                break

            item = array.pop(0)
            length -= 1
            if item is not None:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    def test_min_depth(self):
        s = Solution()

        array = []
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 0)

        array = [1]
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 1)

        array = [1, 2, None]
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 2)

        array = [1, None, 2]
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 2)

        array = [3, 9, 20, None, None, 15, 7]
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 2)

        array = [1, 2, 3, 3, 5, 6, 7, 8, 9, 10]
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 3)

        array = [1, 2, 3, None, None, 3, 8, 9, 0]
        self.assertEqual(s.minDepth(self.create_binary_tree(array)), 2)


if __name__ == "__main__":
    unittest.main()
