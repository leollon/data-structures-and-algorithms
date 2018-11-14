"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

import doctest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> l1 = ListNode(1)
        >>> l1.next = ListNode(2)
        >>> l1.next.next = ListNode(3)

        >>> l2 = ListNode(1)
        >>> l2.next = ListNode(4)
        >>> l2.next.next = ListNode(5)
        >>> l2.next.next.next = ListNode(6)

        >>> l = s.mergeTwoLists(l1, l2)
        >>> while l:
        ...     print(l.val, end='')
        ...     l = l.next
        ...     if not l:
        ...         break
        ...
        1123456
        >>> l1 = ListNode(1)
        >>> l2 = ListNode(1)
        >>> l = s.mergeTwoLists(l1, l2)
        >>> while l:
        ...    print(l.val, end='')
        ...    l = l.next
        ...
        11
        """
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

if __name__ == '__main__':
    doctest.testmod(verbose=True)

