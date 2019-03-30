# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Examples

            >>> s = Solution()
            >>> def create(array):
            ...     t = None
            ...     for val in array:
            ...         new_node = ListNode(val)
            ...         new_node.next = t
            ...         t = new_node
            ...     return t

            >>> nums = []
            >>> head = create(nums)
            >>> head = s.swapPairs(head)
            >>> s.show(head)

            >>> nums = [1]
            >>> head = create(nums)
            >>> head = s.swapPairs(head)
            >>> s.show(head)
            1 

            >>> nums = [1, 2, 3, 4]
            >>> head = create(nums)
            >>> head = s.swapPairs(head)
            >>> s.show(head)
            3 4 1 2 

            >>> nums = [1, 3]
            >>> head = create(nums)
            >>> head = s.swapPairs(head)
            >>> s.show(head)
            1 3 

            >>> nums = [1, 2, 3]
            >>> head = create(nums)
            >>> head = s.swapPairs(head)
            >>> s.show(head)
            2 3 1 

            >>> nums = [2, 5, 3, 4, 6, 2, 2]
            >>> head = create(nums)
            >>> head = s.swapPairs(head)
            >>> s.show(head)
            2 2 4 6 5 3 2 
        """
        if not head:
            return
        pre, nxt = head, head.next
        t = None
        while pre and nxt:
            pre.next = nxt.next  # 记住还未交换结点的开始地址
            nxt.next = pre  # 后续结点变成前续结点
            if t:
                # 从第二次交换以后的每一次交换中，将上一次前续结点经过交换后变成的后继结点
                # 保留下一个结点（next）的地址指向经过本次交换后，后续结点（nxt）变成
                # 前续结点的地址
                t.next = nxt
            if not t:
                # 更改链表头部
                head = nxt
            t = pre  # 保留交换后的后续结点
            pre = pre.next  # 将要交换的前续结点移往下一个结点
            if pre:
                # 未到达尾结点，将要交换的后续结点移往前续结点的后继结点
                nxt = pre.next
        return head

    def show(self, head):
        h = head
        while h:
            print(h.val, end=' ')
            h = h.next


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
