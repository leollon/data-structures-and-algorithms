#!/usr/bin/python3
"""Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its
head.

Example:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

    Given n will always be valid.

Follow up:

    Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        Examples:

            >>> s = Solution()
            >>> head = ListNode(1)
            >>> t, i = head, 2
            >>> while i != 6:
            ...     node = ListNode(i)
            ...     t.next, t = node, node
            ...     i += 1
            ...
            >>> t = head
            >>> while t != None:
            ...     print(t.val, end=' ')
            ...     t = t.next
            ...
            1 2 3 4 5 
            >>> head = s.removeNthFromEnd(head, 3)
            >>> t = head
            >>> while t != None:
            ...     print(t.val, end=' ')
            ...     t = t.next
            ...
            1 2 4 5 
        """
        length = 1
        node_dict = dict()
        pointer = head
        while pointer.next != None and n:
            length += 1
            node_dict[length] = pointer
            pointer = pointer.next
        pos = length - n + 1
        if pos == 1:
            head = head.next
        else:
            prev_node = node_dict[pos]
            prev_node.next = prev_node.next.next
        return head


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
