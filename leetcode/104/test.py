import unittest
from Maximum_Depth_of_Binary_Tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    @staticmethod
    def create_binary_tree(array):
        if not array: return None
        root = TreeNode(array[0])
        node_queue = [root]
        front, index = 0, 1
        sub_array = array[1:]
        while index < len(sub_array):
            node = node_queue[front]
            front += 1
            item = array[index]
            index += 1
            if item:
                node.left = TreeNode(item)
                node_queue.append(node.left)

            if index >= len(sub_array):
                break
            
            item = array[index]
            index += 1
            if item:
                node.right = TreeNode(item)
                node_queue.append(node.right)
        return root

    def test_max_depth(self):
        s = Solution()

        array = [3, 9, 20, None, None, 15, 7]
        root = self.create_binary_tree(array)
        ans = s.maxDepth(root)
        result = 3
        self.assertEqual(result, ans)

        array = []
        root = self.create_binary_tree(array)
        ans = s.maxDepth(root)
        result = 0
        self.assertEqual(result, ans)

        array = [1]
        root = self.create_binary_tree(array)
        ans = s.maxDepth(root)
        result = 1
        self.assertEqual(result, ans)

        array = [1, 2, 1, None, None, 2, 3, 4, 5, 6, 8, 9, None]
        root = self.create_binary_tree(array)
        ans = s.maxDepth(root)
        result = 5
        self.assertEqual(result, ans)

        array = [1, 2, 1, 2, 3, 4, 5, 6, 8, 9, 10, None]
        root = self.create_binary_tree(array)
        ans = s.maxDepth(root)
        result = 4
        self.assertEqual(result, ans)

        array = [
            1, 2, None, 1, None, 2, None, None, 3, None, 4, None, 5, None, 6,
            None, 8, None, 9, None, 10, None
        ]
        root = self.create_binary_tree(array)
        ans = s.maxDepth(root)
        result = 11
        self.assertEqual(result, ans)


if __name__ == "__main__":
    unittest.main()
