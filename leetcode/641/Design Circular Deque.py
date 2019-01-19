"""Design Circular Deque
Design your implementation of the circular double-ended _queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the _queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
 

Note:

    All values will be in the range of [0, 1000].
    The number of operations will be in the range of [1, 1000].
    Please do not use the built-in Deque library.
"""
import unittest


class DataNode:
    def __init__(self, item):
        self._item = item
        self._nxt = None
        self._pre = None


class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._max_length = k
        self._length = 0
        self._first = None
        self._last = None

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        new_node = DataNode(value)
        if self._first is None:
            self._first = new_node
            self._first._nxt = new_node
            self._last = self._first
        else:
            new_node._pre = self._first._pre
            new_node._nxt = self._first
            self._first = new_node
            self._last._nxt = self._first
        self._first._pre = new_node
        self._length += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        new_node = DataNode(value)
        if self._last is None:
            self._last = new_node
            self._last._pre = new_node
            self._first = self._last
        else:
            new_node._nxt = self._last._nxt
            new_node._pre = self._last
            self._last = new_node
            self._first._pre = self._last
        self._last._nxt = new_node
        self._length += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        if self._length == 1:
            self._first = self._last = None
        else:
            self._first = self._first._nxt
            self._first._pre = self._last
            self._last._nxt = self._first
        self._length -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        if self._length == 1:
            self._first = self._last = None
        else:
            self._last = self._last._pre
            self._last._nxt = self._first
            self._first._pre = self._last
        self._length -= 1
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self._first._item
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self._last._item
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self._length == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._max_length == self._length


class TestCircularDequeue(unittest.TestCase):
    
    @staticmethod
    def createCircularDequeue(k):
        return MyCircularDeque(k)

    def test_isEmpty(self):
        # empty queue
        q = self.createCircularDequeue(10)
        self.assertEqual(q.isEmpty(), True)
        # full queue
        i = 10
        while i != 0:
            q.insertFront(i)
            i -= 1
        self.assertEqual(q.isEmpty(), False)


    def test_insertFront(self):
        # empty queue
        q = self.createCircularDequeue(0)
        self.assertEqual(q.insertFront(2), False)
        # queue is full
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertFront(i) 
            i -= 1
        self.assertEqual(q.insertFront(20), False)

        q.deleteFront()
        self.assertEqual(q.insertFront(100), True)

    def test_insertLast(self):
        # empty queue
        q = self.createCircularDequeue(0)
        self.assertEqual(q.insertLast(2), False)
        # queue is full
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertLast(i) 
            i -= 1
        self.assertEqual(q.insertLast(20), False)

        q.deleteLast()
        self.assertEqual(q.insertLast(100), True)

    def test_deleteFront(self):
        # empty queue
        q = self.createCircularDequeue(0)
        self.assertEqual(q.deleteFront(), False)
        # full queue
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertLast(i) 
            i -= 1
        self.assertEqual(q.deleteFront(), True)


    def test_deleteLast(self):
        # empty queue
        q = self.createCircularDequeue(0)
        self.assertEqual(q.deleteLast(), False)
        # full queue
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertLast(i) 
            i -= 1
        self.assertEqual(q.deleteLast(), True)

    def test_isFull(self):
        # empty queue
        q = self.createCircularDequeue(0)
        self.assertEqual(q.isFull(), True)
        # full queue
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertLast(i)
            i -= 1
        self.assertEqual(q.isFull(), True)
        q.deleteLast()
        self.assertEqual(q.isFull(), False)

    def test_getFront(self):
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertFront(i)
            i -= 1
        self.assertEqual(q.getFront(), 1)
        q = self.createCircularDequeue(10)
        self.assertEqual(q.getFront(), -1)


    def test_getRear(self):
        q = self.createCircularDequeue(10)
        i = 10
        while i != 0:
            q.insertLast(i)
            i -= 1
        self.assertEqual(q.getRear(), 1)
        q = self.createCircularDequeue(10)
        self.assertEqual(q.getRear(), -1)

    def test_getRear(self):
        pass



if __name__ == "__main__":
    unittest.main()