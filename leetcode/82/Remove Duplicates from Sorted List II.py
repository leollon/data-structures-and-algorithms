"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:

    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

Example 2:

    Input: 1->1->1->2->3
    Output: 2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Examples

            >>> s = Solution()
            >>> def create(array):
            ...     head = None
            ...     for val in array:
            ...         new_node = ListNode(val)
            ...         if not head:
            ...             head = new_node
            ...             tmp = head
            ...         else:
            ...             tmp.next = new_node
            ...             tmp = new_node
            ...     return head

            >>> nums = []
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)

            >>> nums = [1, 2, 3, 3, 4, 4, 5]
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)
            1 2 5 

            >>> nums = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6]
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)
            1 2 

            >>> nums = [2, 2, 2, 3, 4, 5]
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)
            3 4 5 

            >>> nums = [1, 2, 3, 4, 4, 4, 4]
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)
            1 2 3 

            >>> nums = [1, 1, 1, 1, 1, 1]
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)

            >>> nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]
            >>> head = create(nums)
            >>> head = s.deleteDuplicates(head)
            >>> s.show(head)
            1 



        """
        if not head:
            return
        slow_ptr, fast_ptr = head, head.next
        diff = None
        while fast_ptr:
            if slow_ptr.val != fast_ptr.val:
                diff = slow_ptr
            while fast_ptr and slow_ptr.val == fast_ptr.val:
                # 删除重复元素
                slow_ptr.next = fast_ptr.next
                fast_ptr = fast_ptr.next
                if not diff:
                    # 头节点是重复元素，被删除
                    head = fast_ptr
            if diff:
                # 将剩下的最后一个重复元素也删除
                # 本类diff.next是等于slow_ptr的
                diff.next = fast_ptr
            slow_ptr = fast_ptr  # 移动慢指针指向下一个需要判断是否重复的元素
            if slow_ptr:
                # 未到达尾结点
                fast_ptr = slow_ptr.next
        return head

    def show(self, head):
        ptr = head
        while ptr:
            print(ptr.val, end=' ')
            ptr = ptr.next


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
