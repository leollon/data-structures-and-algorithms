"""Implement Stack using Queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:

    You must use only standard operations of a queue -- which means only push to
    back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively.
    You may simulate a queue by using a list or deque (double-ended queue),
    as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top
    operations will be called on an empty stack).
"""
import unittest


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        tail = len(self.queue) - 1
        while tail > 0:
            self.queue[tail], self.queue[tail-1] = self.queue[tail-1], self.queue[tail]
            tail -= 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


class TestMyStack(unittest.TestCase):

    @staticmethod
    def createStatck():
        return MyStack()
    
    def test_push(self):
        stack = self.createStatck()
        stack.push(2)
        self.assertEqual(stack.top(), 2)

    def test_pop(self):
        stack = self.createStatck()
        stack.push(233)
        self.assertEqual(stack.pop(), 233)
        self.assertEqual(stack.pop(), None)

    def test_empty(self):
        stack = self.createStatck()
        self.assertEqual(stack.empty(), True)
        stack.push(666)
        self.assertEqual(stack.empty(), False)

    def test_top(self):
        stack = self.createStatck()
        stack.push(666)
        self.assertEqual(stack.top(), 666)
        stack.push(888)
        self.assertEqual(stack.top(), 888)


if __name__ == "__main__":
    unittest.main()
