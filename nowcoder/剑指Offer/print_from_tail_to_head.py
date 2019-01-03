# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # first method
        result_list = []
        curr = listNode
        while curr is not None:
            result_list.insert(0, curr.val)
            curr = curr.next # 下一个结点的地址，地址为None的时候，退出循环
        return result_list
