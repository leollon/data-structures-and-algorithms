"""Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionWithRecursion:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rypte: List[int]
        """
        result = []
        if not root:
            return result
        self._helper(root.left, result)  # 左子树
        self._helper(root.right, result)  # 右子树
        result.append(root.val)  # 根结点
        return result

    def _helper(self, node, result):
        if not node:
            return
        self._helper(node.left, result)
        self._helper(node.right, result)
        result.append(node.val)


class SolutionWithIteration:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rypte: List[int]
        """
        result = []
        node = root
        root_nodes = []
        visited_node = []
        while node or root_nodes:
            if node and node.left and node.left not in visited_node:
                # 当前结点存在左结点，不管有没有右结点，都将当前结点放入根结点列表中，然后
                # 继续往下一个左结点走，寻找该子树上面的叶子结点
                root_nodes.append(node)
                node = node.left
                continue
            if node and node.right and node.right not in visited_node:
                # 当前结点没有左结点，但是有右结点，因此也将当前结点放入根结点列表中，然后
                # 往下一个右结点走，寻找该子树上面的叶子结点
                root_nodes.append(node)
                node = node.right
                continue
            if node and not node.left and not node.right:
                result.append(node.val)  # 到达叶子结点
                visited_node.append(node)  # 将访问了的结点放入结果数组中
                if node == root:
                    # 只有一个根结点，此时树的深度为0
                    break
            if root_nodes:
                # 到了叶子结点之后，往根的方向返回
                node = root_nodes.pop()
                while not node.right or node.right in visited_node:
                    # 进行根结点数组的检查，如果存在右子树，或是当前结点的右子树已经
                    # 遍历完了，则将当前结点的值放入结果数组中
                    result.append(node.val)
                    visited_node.append(node)
                    if root_nodes:
                        node = root_nodes.pop()
                    else:
                        break
                if node == root and node in visited_node:
                    # 树的深度大于0的时候，遍历完了左子树和右子树之后
                    # 已经到达树的最上层，也就是最后的根结点
                    break
                root_nodes.append(node)  # 当前结点，也是当前子树的根结点，存在右子树
                node = node.right  # 查找右子树的叶子结点
        return result
