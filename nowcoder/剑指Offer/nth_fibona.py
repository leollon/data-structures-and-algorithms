"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # first method
        sum = 0
        a = 1
        b = 1
        i = 0
        while i < n:
            sum = a
            i += 1
            a, b = b, a+b
        return sum


s = Solution()

print(s.Fibonacci(5))