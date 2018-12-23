#!/usr/bin/python3
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        Examples:

            >>> s = Solution()
            >>> head = ListNode(1)
            >>> t, i = head, 2
            >>> while i != 3:
            ...     node = ListNode(i)
            ...     t.next, t = node, node
            ...     i += 1
            ...
            >>> t = head
            >>> while t:
            ...     print(t.val, end=' ')
            ...     t = t.next
            ... 
            1 2 
            >>> head = s.rotateRight(head, 1)
            >>> t = head
            >>> while t:
            ...     print(t.val, end=' ')
            ...     t = t.next
            ... 
            2 1 
        """
        if not head: return head
        length = 0
        walk_node = head
        while walk_node != None:
            length += 1
            tail = walk_node
            walk_node = walk_node.next
        if length == 1: return head
        k = k % length
        if not k: return head
        count = 0
        walk_node = head
        while count != (length - k):
            count += 1
            new_tail = walk_node
            walk_node = walk_node.next
        new_head, tail.next = new_tail.next, head
        new_tail.next = None
        return new_head


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
