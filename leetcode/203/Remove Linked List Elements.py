"""Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example:

    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
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

        >>> nums, val = [1, 2, 6, 3, 4, 5, 6], 6
        >>> head = create(nums)
        >>> head = s.removeElements(head, val)
        >>> s.show(head)
        1 2 3 4 5 

        >>> nums, val = [1, 1, 2, 1, 3, 4, 4, 5, 5, 6, 6, 6, 6, 6], 1
        >>> head = create(nums)
        >>> head = s.removeElements(head, val)
        >>> s.show(head)
        2 3 4 4 5 5 6 6 6 6 6 

        >>> nums, val = [], 1
        >>> head = create(nums)
        >>> head = s.removeElements(head, val)
        >>> s.show(head)


        >>> nums, val = [1, 1], 1
        >>> head = create(nums)
        >>> head = s.removeElements(head, val)
        >>> s.show(head)
        """
        remember, cursor = None, head
        while cursor:
            if cursor.val == val:
                if cursor == head:
                    head = cursor.next
                    cursor = head
                else:
                    remember.next = cursor.next
                    cursor = remember.next
            else:
                remember = cursor
                cursor = cursor.next
        return head

    def show(self, head):
        tmp = head
        while tmp:
            print(tmp.val, end=' ')
            tmp = tmp.next


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
