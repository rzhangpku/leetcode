# -*- coding:utf-8 -*-


# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r=ListNode(self)
        if l1==None:
            r=l2
            return r
        elif l2==None:
            r=l1
            return r
        if l1.val<l2.val:
            r.val=l1.val
            r.next=Solution.mergeTwoLists(self, l1.next, l2)
        else:
            r.val=l2.val
            r.next=Solution.mergeTwoLists(self, l1, l2.next)
        return r
