import unittest
from binary_tree_inorder_traversal import SolutionWithRecursion, TreeNode


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

    def test_inorder_traversal(self):
        s_recursion = SolutionWithRecursion()

        array = [1, None, 2, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [1, 3, 2]
        )

        array = []
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            []
        )

        array = [1, 2, 2, 3, 4, 4, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [3, 2, 4, 1, 4, 2, 3]
        )

        array = [1, 2, 2, 3, 4, 4, 3, 5, 6, 6, 5, 7, 8, 8, 7]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [5, 3, 6, 2, 6, 4, 5, 1, 7, 4, 8, 2, 8, 3, 7]
        )

        array = [1, 2, 2, 3, 4, 4, 5]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [3, 2, 4, 1, 4, 2, 5]
        )

        array = [1, 2, 2, None, 3, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [2, 3, 1, 3, 2]
        )

        array = [1, 2, 2, 3, None, None, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [3, 2, 1, 2, 3]
        )

        array = [1, 2, 3, None, 3, None, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [2, 3, 1, 3, 3]
        )

        array = [1, 2, 3, 3, None, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [3, 2, 1, 3, 3]
        )

        array = [1, 2, 2, None, 3, 3, None, 4, None, None, 4]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [2, 4, 3, 1, 3, 4, 2]
        )
        array = [1, 2, 2, 3, None, None, 3, None, 4, 4]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.inorderTraversal(root),
            [3, 4, 2, 1, 2, 4, 3]
        )


if __name__ == "__main__":
    unittest.main()
