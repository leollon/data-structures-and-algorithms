import unittest

from binary_tree_postorder_traversal import SolutionWithRecursion, TreeNode


class TestSolution(unittest.TestCase):

    @staticmethod
    def creat_binary_tree(array):
        if not array:
            return None
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

    def test_postorder_traversal(self):
        s_recursion = SolutionWithRecursion()

        array = [1, 0]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [0, 1]
        )

        array = []
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            []
        )

        array = [1, None, 0]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [0, 1]
        )

        array = [2, None, 3, None, 1]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [1, 3, 2]
        )

        array = [2, 3, None, 1]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [1, 3, 2]
        )

        array = [1, None, 2, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [3, 2, 1]
        )

        array = [1, 2, 3, 5, 6, 7, 8]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [5, 6, 2, 7, 8, 3, 1]
        )

        array = [1, 2, 3, None, 8]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [8, 2, 3, 1]
        )

        array = [1, 2, 3, None, None, 7, 8]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [2, 7, 8, 3, 1]
        )

        array = [1, 2, 3, 4, 5]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [4, 5, 2, 3, 1]
        )

        array = [1, 2, 3, None, None, 4]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [2, 4, 3, 1]
        )

        array = [1, 2, 3, None, None, None, 5]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [2, 5, 3, 1]
        )

        array = [1, 2, 3, 5, 6, 7, 8, None,
                 None, 11, 12, 13, 14, 15, 16, 9, 10]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.postorderTraversal(root),
            [5, 9, 10, 11, 12, 6, 2, 13, 14, 7, 15, 16, 8, 3, 1]
        )


if __name__ == "__main__":
    unittest.main()
