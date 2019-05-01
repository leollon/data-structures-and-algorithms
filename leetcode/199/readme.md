```Python
class Solution:
    def rightSideView(self, root):
        result = []
        self._helper(root, result, 0)
        return result

    def _helper(self, node, result, level):
        if not node:
        level += 1
        if len(result) < level:
            # 因为是只取子树的右结点，所以，每将一个右结点的值放入结果中，
            # 导致数组的长度代表当前的子树的深度，或者说子树的层级
            result.append(node.val)
        # 从右子树开始遍历右结点直到叶子结点
        self._helper(node.right, result, level)
        # 因为是从右边开始看，所以右结点有可能挡住左结点，也有可能没有挡住，
        # 所以，还需检查左子树的层级(高度)是否和右子树的层级(高度)是否相等
        self._helper(node.left, result, level)
```