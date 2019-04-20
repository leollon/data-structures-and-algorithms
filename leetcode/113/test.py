import unittest


from path_sum_ii import TreeNode, Solution


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_binary_tree(array):
        if not array:
            return None

        root = TreeNode(array.pop(0))
        node_queue = [root]
        front = index = 0
        while index < len(array):
            node = node_queue[front]
            front += 1
            item = array[index]
            index += 1
            if item:
                node.left = TreeNode(item)
                node_queue.append(node.left)

            if index >= len(array):
                break

            item = array[index]
            index += 1
            if item:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    def test_pathSum(self):
        array, target = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(
            s.pathSum(tree, target),
            [[5, 4, 11, 2], [5, 8, 4, 5]]
        )

        array, target = [1, 2, 3, 4, 5, 6, None,
                         3, 2, None, 2, None, 3, None], 10
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(
            s.pathSum(tree, target),
            [[1, 2, 4, 3], [1, 2, 5, 2]]
        )

        array, target = [1, 2, None, 3, None, 4, None, 5, None], 15
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(
            s.pathSum(tree, target),
            [[1, 2, 3, 4, 5]]
        )

        array, target = [1, None, 3, 5, 4, None, 1, 4, None, 2, None], 12
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(
            s.pathSum(tree, target),
            [[1, 3, 5, 1, 2], [1, 3, 4, 4]]
        )

        array, target = [2, 3, 2], 5
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.pathSum(tree, target), [[2, 3]])

        array, target = [2], 2
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.pathSum(tree, target), [[2]])

        array, target = [], 2
        tree = self.create_binary_tree(array)
        s = Solution()
        self.assertEqual(s.pathSum(tree, target), [])


if __name__ == "__main__":
    unittest.main()
