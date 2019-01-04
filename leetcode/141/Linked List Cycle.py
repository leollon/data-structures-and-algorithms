#!/usr/bin/python3
"""Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where tail
connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to
the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to
the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

    Can you solve it using O(1) (i.e. constant) memory?
"""
import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        first = head
        second = head.next
        while first != second:
            if (not second or not second.next):
                return False
            first = first.next
            second = second.next.next
        return True


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_set = set()
        first = head
        while first:
            if first in node_set:
                return True
            node_set.add(first)
            first = first.next
        return False


class TestSolution2(unittest.TestCase):

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
        array = [3, 2, 0, -4]
        position = 1
        head = self.createLinkedList(array, position)
        self.assertEqual(True, Solution2().hasCycle(head))

        array = [1]
        position = -1
        head = self.createLinkedList(array, position)
        self.assertEqual(False, Solution2().hasCycle(head))

        array = [2, 1]
        position = 0
        head = self.createLinkedList(array, position)
        self.assertEqual(True, Solution2().hasCycle(head))



if __name__ == "__main__":
    unittest.main()