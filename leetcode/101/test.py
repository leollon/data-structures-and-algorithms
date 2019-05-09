import unittest

from symmetric_tree import SolutionWithRecursion, TreeNode


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_binary_tree(array):
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

    def test_is_symmetric(self):

        s = SolutionWithRecursion()

        array = [1, 2, 2, 3, 4, 4, 3]
        root = self.create_binary_tree(array)
        self.assertEqual(s.isSymmetric(root), True)

        array = [1, 2, 2, None, 3, None, 3]
        root = self.create_binary_tree(array)
        self.assertEqual(s.isSymmetric(root), False)

        array = [1, 2, 2, None, 3, 3]
        root = self.create_binary_tree(array)
        self.assertEqual(s.isSymmetric(root), True)

        array = [1, 2, 2, 3, None, 3]
        root = self.create_binary_tree(array)
        self.assertEqual(s.isSymmetric(root), False)

        array = [1, 2, 2, 3, 4, 4, 5]
        root = self.create_binary_tree(array)
        self.assertEqual(s.isSymmetric(root), False)


if __name__ == "__main__":
    unittest.main()
