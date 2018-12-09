"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
import doctest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        >>> s = Solution()

        Examples:
            >>> l1 = ListNode(2)
            >>> l1.next = ListNode(4)
            >>> l1.next.next = ListNode(3)
            >>> l2 = ListNode(5)
            >>> l2.next = ListNode(6)
            >>> l2.next.next = ListNode(4)
            >>> l = s.addTwoNumbers(l1, l2)
            >>> while l:
            ...     print(l.val, end='')
            ...     l = l.next
            708
            >>> l1 = ListNode(1)
            >>> l1.next = ListNode(8)
            >>> l2 = ListNode(0)
            >>> l = s.addTwoNumbers(l1, l2)
            >>> while l:
            ...     print(l.val, end='')
            ...     l = l.next
            18
        """
        head = ListNode(0)
        tmp = head
        carry = 0
        p, q = l1, l2
        while p or q:
            x, y = p.val if (p is not None) else 0, q.val if (q is not None) else 0
            new_node = ListNode(sum([x, y, carry]) % 10)
            carry = sum([x, y, carry]) // 10
            tmp.next = new_node
            tmp = new_node
            p = p.next if p else None
            q = q.next if q else None
        if carry:
            new_node = ListNode(carry)
            tmp.next = new_node
        return head.next


if __name__ == '__main__':
    doctest.testmod(verbose=True)
