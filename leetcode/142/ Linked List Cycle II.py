# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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


def createLinkedList(array, position):
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


def testHasCycle():
    array = [3, 2, 0, -4, 8, 9]
    position = 4
    head = createLinkedList(array, position)
    s = Solution().detectCycle(head)
    print(s.val)

    array = [2, 1]
    position = 0
    head = createLinkedList(array, position)
    s = Solution().detectCycle(head)
    print(s.val)

    array = [3, 2, 0, -4]
    position = 2
    head = createLinkedList(array, position)
    s = Solution().detectCycle(head)
    print(s.val)

    array = [1]
    position = -1
    head = createLinkedList(array, position)
    s = Solution().detectCycle(head)
    print(s)


if __name__ == "__main__":
    testHasCycle()
