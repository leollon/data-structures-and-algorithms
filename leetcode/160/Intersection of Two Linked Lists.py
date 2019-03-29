# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = len_b = 1
        a, b = headA, headB
        while a and b:
            if a.next:
                a = a.next
                len_a += 1
            if b.next:
                b = b.next
                len_b += 1
            if not a.next and not b.next:
                break
        if a != b:
            return None
        a, b = headA, headB
        if len_a > len_b:
            length = len_a - len_b
        else:
            length = len_b - len_a
        while length > 0 and a and b:
            if len_a > len_b:
                a = a.next
            elif len_a < len_b:
                b = b.next
            length -= 1
        while a != b and a and b:
            a = a.next
            b = b.next
        return a and b
