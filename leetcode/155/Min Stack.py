"""Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
"""
import unittest


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


class TestMinStack(unittest.TestCase):
    
    @staticmethod
    def createStack():
        return MinStack()

    def test_function(self):
        stack = self.createStack()
        stack.push(0)
        stack.push(1)
        stack.push(8)
        self.assertEqual(stack.top(), 8)
        self.assertEqual(stack.getMin(), 0)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.top(), 1)


if __name__ == "__main__":
    unittest.main()
