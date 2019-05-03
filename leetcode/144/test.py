import unittest

from binary_tree_preorder_traversal import SolutionWithRecursion,\
    SolutionWithIteration, TreeNode


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

    def test_preorder_traversal(self):
        s_recursion = SolutionWithRecursion()
        s_iteration = SolutionWithIteration()

        array = [1, None, 2, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = []
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 2, 3, 4, 4, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 2, 3, 4, 4, 3, 5, 6, 6, 5, 7, 8, 8, 7]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 2, 3, 4, 4, 5]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 2, None, 3, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 2, 3, None, None, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 3, None, 3, None, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 3, 3, None, 3]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )

        array = [1, 2, 2, None, 3, 3, None, 4, None, None, 4]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )
        array = [1, 2, 2, 3, None, None, 3, None, 4, 4]
        root = self.creat_binary_tree(array)
        self.assertEqual(
            s_recursion.preorderTraversal(root),
            s_iteration.preorderTraversal(root)
        )


if __name__ == "__main__":
    unittest.main()
