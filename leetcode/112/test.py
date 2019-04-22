import unittest


from path_sum import TreeNode, Solution


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_binary_tree(array):
        if not array:
            return None
        root = TreeNode(array[0])
        node_queue = [root]
        front, index = 0, 1
        sub_array = array[1:]
        while index < len(sub_array):
            node = node_queue[front]
            front += 1
            item = array[index]
            index += 1
            if item is not None:
                node.left = TreeNode(item)
                node_queue.append(node.left)

            if index >= len(sub_array):
                break

            item = array[index]
            index += 1
            if item is not None:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    def test_hasPathSum(self):
        array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        target = 22
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), True)

        array = [5, None, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        target = 13
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), False)

        array = [5, None, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        target = 22
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), False)

        array = [2, 3, 2]
        target = 5
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), True)

        array = [2, 3, 2]
        target = 2
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), False)

        array = [2]
        target = 2
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), True)

        array = [1, -1, 3, -3, None, 3, None, 3, -6, None, 2, 3, 5, None]
        target = -9
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), True)

        array = []
        target = 1
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.hasPathSum(tree, target), False)


if __name__ == "__main__":
    unittest.main()
