"""Design Linked List
hould have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node. 
If you want to use the doubly linked list, you will need one more attribute
prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list.
If the index is invalid, return -1.

addAtHead(val) : Add a node of value val before the first element of the linked
list. After the insertion, the new node will be the first node of the linked
list.

addAtTail(val) : Append a node of value val to the last element of the linked list.

addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.

deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Note:

    1. All values will be in the range of [1, 1000].
    2. The number of operations will be in the range of [1, 1000].
    3. Please do not use the built-in LinkedList library.
"""


class MyLinkedList:

    class DataNode:
        def __init__(self, item):
            self._item = item
            self._next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._size = 0
        self._first = None
        self._last = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self._size or not self._size or index < 0:
            # index is invalid, or empty linked list
            return -1
        pos = 0
        head = self._first
        while pos < index:
            head = head._next
            pos += 1
        return head._item

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = self.DataNode(val)
        new_node._next = self._first
        self._first = new_node
        if not self._last:
            # 空链表
            self._last = new_node
        self._size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = self.DataNode(val)
        if self._last:
            # 非空链表
            self._last._next = new_node
        else:
            # 空链表
            self._first = new_node
        self._last = new_node
        self._size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index >= self._size + 1 or index < 0: return
        done = False
        if not self._size:
            # 空链表
            self._first = self._last = self.DataNode(val)
            self._size += 1
            done = True

        if index == 0 and not done:
            self.addAtHead(val)
            done = True

        if index == self._size and not done:
            self.addAtTail(val)
            done = True

        pos = 0
        prev, inserted, new_node = None, self._first, self.DataNode(val)

        while not done:
            if pos == index:
                new_node._next = inserted
                prev._next = new_node
                done = True
                self._size += 1
            else:
                pos += 1
                prev = inserted
                if inserted:
                    inserted = inserted._next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self._size or index < 0 or not self._size:
            # index is invalid, or empty linked list
            return
        prev, deleted = None, self._first
        pos = 0
        while pos < index:
            pos += 1
            prev = deleted
            deleted = deleted._next
        if not index:
            # 删除首结点
            deleted = deleted._next
            self._first = deleted
            if not self._first:
                self._last = None
        else:
            prev._next = deleted._next
            if not prev._next:
                self._last = prev
        self._size -= 1

    def clear(self):
        while self._first:
            self._first = self._first._next
            self._size -= 1
        self._last = self._first

