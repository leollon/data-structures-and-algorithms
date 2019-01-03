#!/usr/bin/python3
"""reversed linked list
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

    A linked list can be reversed either iteratively or recursively. Could you
    implement both?
"""
import unittest
from random import randint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    # Iterative version
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        first = head
        reverse = None
        while first:
            second = first.next   # 保存后面所有结点的开始结点
            first.next = reverse  # 将当前结点的指针指向前一个结点
            reverse = first       # 移动到下一个已经更改指针方向的结点
            first = second        # 将结点移动到下一个需要更改指针的结点
        return reverse


class Solution2:
    # Reversive version
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head         # 空链表
        if not head.next: return head    # 到达尾结点
        second = head.next               # 保存当前结点指向后续结点的指针
        rest = self.reverseList(second)  # 继续往后续结点进行递归，子问题方向，最终返回的尾结点是头结点
        second.next = head               # 将子问题的结点的指针指向父问题的结点
        head.next = None                 # 将父问题的结点的指针设置为None
        return rest                      # 一直返回尾结点，递归结束就是尾结点就是首结点


class TestBase:

    def create_linked_list(self, array):
        head = ListNode(array[0])
        t = head
        for i in range(1, len(array)):
            new_node = ListNode(array[i])
            t.next = new_node
            t = new_node
        return head


class TestSolution1(unittest.TestCase, TestBase):

    def test_reverse_linked_list(self):
        # Iterative version
        array = [val for val in range(1, randint(1, 101))]
        head = self.create_linked_list(array)
        s = Solution1()
        head = s.reverseList(head)
        result = []
        while head:
            result.append(head.val)
            head = head.next
        self.assertEqual(list(reversed(array)), result)

class TestSolution2(unittest.TestCase, TestBase):

    def test_reverse_linked_list(self):
        # Recursive version
        array = [val for val in range(1, randint(1, 101))]
        head = self.create_linked_list(array)
        s = Solution2()
        head = s.reverseList(head)
        result = []
        while head:
            result.append(head.val)
            head = head.next
        self.assertEqual(list(reversed(array)), result)


if __name__ == "__main__":
    unittest.main()
