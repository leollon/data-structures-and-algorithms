#!/usr/bin/python3
"""Linked List Cycle II
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where tail
connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the
            second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the
            first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Follow up:
    Can you solve it without using extra space?
"""
import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MySolution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        first = head
        nodes_set = set()
        while first:
            if first in nodes_set:
                return first
            nodes_set.add(first)
            first = first.next
        return None


class BestSolution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        left, right = head, head
        cycle = False
        while True:
            if not right or not right.next:
                break
            left = left.next
            right = right.next.next
            if left == right:
                cycle = True
                left = head
                break
        while cycle:
            if left == right:
                return left
            left = left.next
            right = right.next
        return None


class TestBestSolution(unittest.TestCase):

    def createLinkedList(self, array, position):
        head = ListNode(array[0])
        first = head
        cyclic_start = None
        pos = 0
        for val in array[1:]:
            if (pos == position):
                cyclic_start = first
            last = first
            first.next = ListNode(val)
            first = first.next
            pos += 1
        if cyclic_start:
            last.next = cyclic_start
        return head


    def testHasCycle(self):
        array = [3, 2, 0, -4, 8, 9, 7]
        position = 2
        head = self.createLinkedList(array, position)
        s = MySolution().detectCycle(head)
        self.assertEqual(s.val, 0)
        s = BestSolution().detectCycle(head)
        self.assertEqual(s.val, 0)

        array = [2, 1]
        position = 0
        head = self.createLinkedList(array, position)
        s = MySolution().detectCycle(head)
        self.assertEqual(s.val, 2)
        s = BestSolution().detectCycle(head)
        self.assertEqual(s.val, 2)

        array = [3, 2, 0, -4]
        position = 2
        head = self.createLinkedList(array, position)
        s = MySolution().detectCycle(head)
        self.assertEqual(s.val, 0)
        s = BestSolution().detectCycle(head)
        self.assertEqual(s.val, 0)


        array = [3, 2, 0, -4]
        position = -1
        head = self.createLinkedList(array, position)
        s = MySolution().detectCycle(head)
        self.assertEqual(s, None)
        s = BestSolution().detectCycle(head)
        self.assertEqual(s, None)

        array = [1]
        position = -1
        head = self.createLinkedList(array, position)
        s = MySolution().detectCycle(head)
        self.assertEqual(s, None)
        s = BestSolution().detectCycle(head)
        self.assertEqual(s, None)


if __name__ == "__main__":
    unittest.main()
