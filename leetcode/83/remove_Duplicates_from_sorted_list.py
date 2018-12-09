"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

import doctest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: 

        Examples:
            >>> def my_print(head):
            ...     while True:
            ...         print(head.val, end='')
            ...         head = head.next
            ...         if not head:
            ...             break
            ...
            >>> s = Solution()
            >>> l = ListNode(1)
            >>> l.next = ListNode(2)
            >>> l.next.next = ListNode(2)
            >>> l.next.next.next = ListNode(3)
            >>> l.next.next.next.next = ListNode(3)
            >>> l.next.next.next.next.next = ListNode(4)
            >>> head = s.deleteDuplicates(l)
            >>> my_print(head)
            1234
            >>> l = ListNode(1)
            >>> l.next = ListNode(1)
            >>> l.next.next = ListNode(2)
            >>> head = s.deleteDuplicates(l)
            >>> my_print(head)
            12
            >>> l = ListNode(5)
            >>> l.next = ListNode(4)
            >>> l.next.next = ListNode(2)
            >>> l.next.next.next = ListNode(2)
            >>> l.next.next.next.next = ListNode(2)
            >>> head = s.deleteDuplicates(l)
            >>> my_print(head)
            542
        """
        if not head:
            return head
        node1 = head
        node2 = node1.next
        while node2:
            nxt = node2.next
            if node2.val == node1.val:
                node1.next = nxt
                node2 = nxt
            else:
                node1 = node2
                node2 = nxt
        return head


if __name__ == "__main__":
    doctest.testmod(verbose=True)
