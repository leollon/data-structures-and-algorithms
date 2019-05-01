import unittest

from binary_tree_right_side_view import Solution, TreeNode


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

    def test_right_side_view(self):
        s = Solution()

        # Never have a tree
        array = []
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [])

        # The number of leaves of left subtree is equal to right subtree
        array = [1, 2, 3, None, 5, None, 4]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 3, 4])

        # There is only left subtree, that has two leaves
        array = [1, 2, None, 5, 4, None]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 2, 4])

        # The number of leaves of left subtree is greater than the number
        # of right subtree's leaves
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 3, 7, 10])

        # Full binary tree, the number of left subtree's leaves is
        # equal to the number of right subtree'leaves
        array = [1, 2, 3, 4, 5, 6, 7]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 3, 7])
        [1, 2, 3, None, 5, None, 4]

        # The number of leaves of left subtree is greater than the number
        # of right subtree's leaves
        array = [1, 3, 2, None, 3, None, 4, None, 6]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 2, 4, 6])

        # The number of leaves of left subtree is less than the number
        # of right subtree's leaves
        array = [1, 3, 2, None, 3, None, 4, None, None, 6]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 2, 4, 6])
        [1, 2, 3, None, 5, None, 4]

        # There is only left subtree, each node has two nodes fron root(exclude) to
        # leaf(exclude)
        array = [1, 2, None, 3, 4, 5, 8, None, None, 7, 9]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 2, 4, 8, 9])

        # There is only right subtree
        array = [1, None, 3, None, 4, None, 6, None, 8]
        root = self.create_binary_tree(array)
        self.assertEqual(s.rightSideView(root), [1, 3, 4, 6, 8])


if __name__ == "__main__":
    unittest.main()
