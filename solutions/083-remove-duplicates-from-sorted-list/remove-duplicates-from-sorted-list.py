# -*- coding:utf-8 -*-


# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        if head.next!=None:
            if head.val==head.next.val:
                head.next=head.next.next
                Solution.deleteDuplicates(self, head)
            else:
                Solution.deleteDuplicates(self, head.next)
        return head
