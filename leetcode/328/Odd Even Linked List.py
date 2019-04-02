"""Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the
even nodes. Please note here we are talking about the node number and not the
value in the nodes.

You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:

    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL
Note:

    The relative order inside both the even and odd groups should remain as
    it was in the input.
    The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Examples

        >>> s = Solution()
        >>> def create(array):
        ...     head = tmp = None
        ...     for val in array:
        ...         new_node = ListNode(val)
        ...         if not head:
        ...             head = new_node
        ...         else:
        ...             tmp.next = new_node
        ...         tmp = new_node
        ...     return head

        >>> nums = []
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)

        >>> nums = [1, 2, 3, 4, 5]
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)
        1 3 5 2 4 

        >>> nums = [1, 2, 3]
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)
        1 3 2 

        >>> nums = [1, 2, 3, 4, 5, 6, 7]
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)
        1 3 5 7 2 4 6 

        >>> nums = [1, 2, 3, 4, 5, 6, 7, 8]
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)
        1 3 5 7 2 4 6 8 

        >>> nums = [1, 2]
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)
        1 2 

        >>> nums = [1]
        >>> head = create(nums)
        >>> head = s.oddEvenList(head)
        >>> s.show(head)
        1 

        """
        if not head or not head.next:
            return head
        odd, even = head, head.next
        odd_cursor, even_cursor = even.next, even
        while odd_cursor:
            tmp = odd_cursor.next
            odd_cursor.next = even
            odd.next = odd_cursor
            odd = odd_cursor
            even_cursor.next = tmp
            even_cursor = tmp
            if not tmp:
                break
            tmp = tmp.next
            odd_cursor = tmp
        return head

    def show(self, head):
        tmp = head
        while tmp:
            print(tmp.val, end=' ')
            tmp = tmp.next


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
