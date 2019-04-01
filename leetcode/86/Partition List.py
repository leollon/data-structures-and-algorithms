"""Partition List
Given a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

Example:

    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Examples

            >>> s = Solution()
            >>> def create(array):
            ...     head = tmp = None
            ...     for val in array:
            ...         new_node = ListNode(val)
            ...         if not tmp:
            ...             head = new_node
            ...             tmp = head
            ...         else:
            ...             tmp.next = new_node
            ...             tmp = new_node
            ...     return head

            >>> nums, x = [1, 4, 3, 2, 5, 2], 1
            >>> linkedlist = create(nums)
            >>> new = s.partition(linkedlist, x)
            >>> s.show(new)
            1 4 3 2 5 2 

            >>> nums, x = [1, 4, 3, 2, 5, 2], 6
            >>> linkedlist = create(nums)
            >>> new = s.partition(linkedlist, x)
            >>> s.show(new)
            1 4 3 2 5 2 

            >>> nums, x = [1, 4, 3, 2, 5, 2], 3
            >>> linkedlist = create(nums)
            >>> new = s.partition(linkedlist, x)
            >>> s.show(new)
            1 2 2 4 3 5 

            >>> nums, x = [8, 7, 6, 5, 4, 3, 2, 1], 5
            >>> linkedlist = create(nums)
            >>> new = s.partition(linkedlist, x)
            >>> s.show(new)
            4 3 2 1 8 7 6 5 

            >>> nums, x = [8, 7, 6, 5, 4, 3, 2, 1], 8
            >>> linkedlist = create(nums)
            >>> new = s.partition(linkedlist, x)
            >>> s.show(new)
            7 6 5 4 3 2 1 8 

            >>> nums, x = [8, 7, 6, 5, 4, 3, 2, 1], 9
            >>> linkedlist = create(nums)
            >>> new = s.partition(linkedlist, x)
            >>> s.show(new)
            8 7 6 5 4 3 2 1 
        """
        if not head:
            return
        dummy = ListNode(0)
        ptr = dummy
        remember, cursor = head, head
        while cursor:
            if cursor.val < x:
                if cursor == head:
                    # 如果是或者一直都是头结点
                    head = cursor.next
                    ptr.next = cursor
                    ptr = cursor
                    cursor = head
                else:
                    # 非头结点
                    remember.next = cursor.next
                    ptr.next = cursor
                    ptr = cursor
                    cursor = remember.next
            else:
                remember = cursor
                cursor = cursor.next
        ptr.next = head
        return dummy.next

    def show(self, head):
        tmp = head
        while tmp:
            print(tmp.val, end=' ')
            tmp = tmp.next


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
