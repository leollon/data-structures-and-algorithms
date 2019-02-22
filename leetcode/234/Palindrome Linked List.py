"""Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        if not head or not head.next:
            return True
        length, cursor = 0, 1
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        second = reverse = None
        first = head
        while cursor <= (length // 2):
            second = first.next
            first.next = reverse
            reverse = first
            first = second
            cursor += 1
        if length % 2:
            second = second.next
        while second:
            if reverse.val != second.val:
                return False
            reverse = reverse.next
            second = second.next
        return True


class TestSolution(unittest.TestCase):
    @staticmethod
    def create_linked_list(array):
        next_node = None
        for num in array:
            new_node = ListNode(num)
            new_node.next = next_node
            next_node = new_node
        return next_node

    def test_even_nodes(self):
        s = Solution()
        array = [1, 4, -1, -1, 4, 1]
        head = self.create_linked_list(array)
        self.assertEqual(True, s.isPalindrome(head))

        array = [1, 2]
        head = self.create_linked_list(array)
        self.assertEqual(False, s.isPalindrome(head))

        array = [1, 1, 2, 1]
        head = self.create_linked_list(array)
        self.assertEqual(False, s.isPalindrome(head))

        array = [1, 2, 1, 1]
        head = self.create_linked_list(array)
        self.assertEqual(False, s.isPalindrome(head))

        array = [
            -31900, 22571, -31634, 19735, 13748, 16612, -28299, -16628, 9614,
            -14444, -14444, 9614, -16628, -31900, 16612, 13748, 19735, -31634,
            22571, -28299
        ]
        head = self.create_linked_list(array)
        self.assertEqual(False, s.isPalindrome(head))

        array = []
        head = self.create_linked_list(array)
        self.assertEqual(True, s.isPalindrome(head))

    def test_odd_nodes(self):
        s = Solution()
        array = [1, 3, 1]
        head = self.create_linked_list(array)
        self.assertEqual(True, s.isPalindrome(head))

        array = [-1, -2, 3, -1,-2]
        head = self.create_linked_list(array)
        self.assertEqual(False, s.isPalindrome(head))

        array = [1, 2, 3, 2, 1]
        head = self.create_linked_list(array)
        self.assertEqual(True, s.isPalindrome(head))
        
        array = [1, 3, 2, 5, 3, 2, 1]
        head = self.create_linked_list(array)
        self.assertEqual(False, s.isPalindrome(head))

        array = [1]
        head = self.create_linked_list(array)
        self.assertEqual(True, s.isPalindrome(head))


if __name__ == "__main__":
    unittest.main()
