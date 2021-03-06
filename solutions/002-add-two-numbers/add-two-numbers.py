# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.carry=0
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1!=None or l2!=None:
            if l1==None:
                s=l2.val+self.carry
                if s>=10:
                    s-=10
                    self.carry=1
                else:
                    self.carry=0
                r=ListNode(s)
                r.next=Solution.addTwoNumbers(self, l1, l2.next)
            elif l2==None:
                s=l1.val+self.carry
                if s>=10:
                    s-=10
                    self.carry=1
                else:
                    self.carry=0
                r=ListNode(s)
                r.next=Solution.addTwoNumbers(self, l1.next, l2)
            else:
                s=l1.val+l2.val+self.carry
                if s>=10:
                    s-=10
                    self.carry=1
                else:
                    self.carry=0
                r=ListNode(s)
                r.next=Solution.addTwoNumbers(self, l1.next, l2.next)
            return r
        else:
            if self.carry==0:
                return None
            else:
                return ListNode(self.carry)
