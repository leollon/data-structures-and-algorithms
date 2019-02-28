#!/usr/bin/python3
"""Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
import unittest


class ListNode:
    def __init__(self, item):
        self._item = item
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return
        if not head.next: return head
        cursor = 1
        first, second = head, head.next
        prev, tail = None, head
        while cursor < n and second:
            if cursor >= m:
                tail.next = second.next
                second.next = first
                first = second
                second = tail.next
                if m != 1:
                    prev.next = first
            else:
                prev = first
                first = first.next
                tail = first
                second = second.next
            cursor += 1
        if m == 1: head = first
        if not second: tail.next = None
        return head


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_linkedlist(size=10):
        next_node = None
        while size > 0:
            new_node = ListNode(size)
            new_node.next = next_node
            next_node = new_node
            size -= 1
        return next_node

    def test_reverse(self):
        s = Solution()

        # m > 1 and n < length
        m, n = 2, 8
        head = self.create_linkedlist()
        head = s.reverseBetween(head, m, n)
        
        result = [1, 8, 7, 6, 5, 4, 3, 2, 9, 10]
        ans = []
        while head:
            ans.append(head._item)
            head = head.next
        self.assertEqual(result, ans)

        # m > 1 and n = length
        m, n = 3, 10
        head = self.create_linkedlist()
        head = s.reverseBetween(head, m, n)
        
        result = [1, 2, 10, 9, 8, 7, 6, 5, 4, 3]
        ans = []
        while head:
            ans.append(head._item)
            head = head.next
        self.assertEqual(result, ans)

        # m = 1 and n < length
        m, n = 1, 9
        head = self.create_linkedlist()
        head = s.reverseBetween(head, m, n)

        result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
        ans = []
        while head:
            ans.append(head._item)
            head = head.next
        self.assertEqual(result, ans)

        # m = 1 and n = length
        m, n = 1, 10
        head = self.create_linkedlist()
        head = s.reverseBetween(head, m, n)

        result = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans = []
        while head:
            ans.append(head._item)
            head = head.next
        self.assertEqual(result, ans)


if __name__ == "__main__":
    unittest.main()
