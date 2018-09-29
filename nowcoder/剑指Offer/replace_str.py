'''
题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # first method
        # return s.replace(' ', '%20')

        sub_str = "%20"
        # second method

        # l = s.split(' ')
        # return sub_str.join(l)
        
        # third method
        new_str = ''
        for i in s:
            if i == ' ':
                new_str += sub_str
            else:
                new_str += i
        return new_str

s = Solution()

str = 'we are happy'

s = s.replaceSpace(str)
print(s)
