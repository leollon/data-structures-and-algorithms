#!/usr/bin/env python3
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        new_root = TreeNode()
        parent_node_stack = []
        curr_node = root
        prev_node = root

        while curr_node:

            if curr_node.left:
                # 找到第一个没有左子树的结点
                p = curr_node
                parent_node_stack.append(curr_node)
                curr_node = curr_node.left
                p.left = None
                continue
            if new_root is None:
                # 创建新二叉树的树根
                new_root = curr_node
            else:
                # 已经建立了新树根
                prev_node.right = curr_node
            # 移动到下一个结点
            prev_node = curr_node
            # 当前结点可能存在右子树
            curr_node = curr_node.right
            if curr_node is None and parent_node_stack:
                # 如果当前结点没有右子树，则返回当前结点的父结点
                curr_node = parent_node_stack.pop()
            else:
                # 将当前结点的指向右子树指针设置为 None，避免循环遍历
                prev_node.right = None

        return new_root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def _build_tree(self, array):
        array_index, node_index, length = 1, 0, len(array)
        root = TreeNode(array[0])
        node_list = [root]
        while array_index < length:
            curr_node = node_list[node_index]

            val = array[array_index]
            if val:
                curr_node.left = TreeNode(val)
                node_list.append(curr_node.left)
            array_index += 1

            if array_index == length:
                break

            val = array[array_index]
            if val:
                curr_node.right = TreeNode(val)
                node_list.append(curr_node.right)
            array_index += 1
            node_index += 1
        return root

    def _traverse(self, root, result):
        if not root:
            return
        result.append(root.val)
        result.append(None)
        self._traverse(root.right, result)

    def test_increasingBST(self):

        array = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
        root = self._build_tree(array)
        result = [
            1, None, 2, None, 3, None, 4, None, 5,
            None, 6, None, 7, None, 8, None, 9]
        traversal = []
        self._traverse(self.solution.increasingBST(root), traversal)
        self.assertEqual(result, traversal)


if __name__ == "__main__":
    unittest.main()

