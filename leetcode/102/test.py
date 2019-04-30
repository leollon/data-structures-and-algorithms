import unittest

from binary_tree_level_order_traversal import Solution, TreeNode


class TestSolution(unittest.TestCase):

    @staticmethod
    def creat_binary_tree(array):
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

    def test_level_order(self):

        s = Solution()

        array = [3, 9, 20, None, None, 15, 7]
        root = self.creat_binary_tree(array)
        self.assertEqual(s.levelOrder(root), [[3], [9, 20], [15, 7]])

        array = [3, 9, 20, None, 15, 7, None]
        root = self.creat_binary_tree(array)
        self.assertEqual(s.levelOrder(root), [[3], [9, 20], [15, 7]])

        array = [1, None, 2]
        root = self.creat_binary_tree(array)
        self.assertEqual(s.levelOrder(root), [[1], [2]])

        array = [1, 2, None]
        root = self.creat_binary_tree(array)
        self.assertEqual(s.levelOrder(root), [[1], [2]])

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        root = self.creat_binary_tree(array)
        self.assertEqual(s.levelOrder(root), [
                         [1], [2, 3], [4, 5, 6, 7], [8, 9]])


if __name__ == "__main__":
    unittest.main()
