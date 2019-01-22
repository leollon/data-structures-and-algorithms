"""Implement Queue using Stacks
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:

    You must use only standard operations of a stack -- which means only push
to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively.
    You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
"""
import unittest


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        tail = len(self.stack) - 1
        while tail > 0:
            self.stack[tail - 1], self.stack[tail] = self.stack[tail], self.stack[tail - 1]
            tail -= 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty(): return None
        return self.stack.pop(-1)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty(): return None
        return self.stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


class TestMyQueue(unittest.TestCase):

    @staticmethod
    def createQueue():
        return MyQueue()

    def test_push(self):
        queue = self.createQueue()
        queue.push(12)
        self.assertEqual(queue.peek(), 12)
        queue.push(233)
        self.assertEqual(queue.peek(), 12)

    def test_pop(self):
        queue = self.createQueue()
        item = 3
        while item > 0:
            queue.push(item)
            item -= 1
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), None)

    def test_top(self):
        queue = self.createQueue()
        item = 3
        while item > 0:
            queue.push(item)
            item -= 1
        self.assertEqual(queue.peek(), 3)


if __name__ == "__main__":
    unittest.main()
