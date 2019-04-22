import unittest

from binary_tree_paths import TreeNode, Solution


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_binary_tree(array):
        root = TreeNode(array.pop(0))
        node_queue = [root]
        index = front = 0
        while index < len(array):
            node = node_queue[front]
            front += 1
            item = array[index]
            index += 1
            if item is not None:
                node.left = TreeNode(item)
                node_queue.append(node.left)

            if index >= len(array):
                break

            item = array[index]
            index += 1
            if item is not None:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    def test_binary_tree_paths(self):
        s = Solution()

        array = [1, 2, 3, None, 5]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.binaryTreePaths(tree), ["1->2->5", "1->3"])

        array = [1, 2, None, 3, 5]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.binaryTreePaths(tree), ["1->2->3", "1->2->5"])

        array = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
        tree = self.create_binary_tree(array)
        self.assertEqual(
            s.binaryTreePaths(tree),
            ["1->2->5->9", "1->2->5->10", "1->2->6->11", "1->3->7", "1->3->8"]
        )

        array = [1, None, 5]
        tree = self.create_binary_tree(array)
        self.assertEqual(s.binaryTreePaths(tree), ["1->5"])


if __name__ == "__main__":
    unittest.main()
