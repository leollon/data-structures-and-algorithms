"""Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
import unittest
from random import randint


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
        """
        stack1, stack2 = [], []
        p, q = l1, l2
        remaining = 0
        while p:
            stack1.append(p.val)
            p = p.next
        while q:
            stack2.append(q.val)
            q = q.next
        next_node = None
        while stack1 or stack2:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            new_node = ListNode((v1 + v2 + remaining) % 10)
            remaining = (v1 + v2 + remaining) // 10
            new_node.next = next_node
            next_node = new_node
        if remaining:
            new_node = ListNode(remaining)
            new_node.next = next_node
            next_node = new_node
        return next_node


class TestSolution(unittest.TestCase):

    @staticmethod
    def create_linkedlist(array):
        next_node = None
        for num in array[::-1]:
            new_node = ListNode(num)
            new_node.next = next_node
            next_node = new_node
        return next_node

    @staticmethod
    def generate_result(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_different_length(self):
        array1, array2 = [7, 2, 4, 3], [5, 6, 4]
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([7, 8, 0, 7], self.generate_result(head))

        array1, array2 = [9, 9, 9], [1]
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([1, 0, 0, 0], self.generate_result(head))
        
        array1, array2 = [1], [9, 9, 9]
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([1, 0, 0, 0], self.generate_result(head))

        array1, array2 = [], [1]
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([1], self.generate_result(head))


    def test_same_length(self):
        array1, array2 = [8, 8, 9], [1, 1, 1]
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([1, 0, 0, 0], self.generate_result(head))

        array1, array2 = [1, 2, 3], [3, 2, 1]
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([4, 4, 4], self.generate_result(head))

        array1, array2 = [], []
        l1, l2 = self.create_linkedlist(array1), self.create_linkedlist(array2)
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual([], self.generate_result(head))


if __name__ == "__main__":
    unittest.main()
