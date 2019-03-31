# -*- coding:utf-8 -*-


# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        if head.next==None:
            return head
        rhead=ListNode(head.val)
        rhead.next=None
        while head.next!=None:
            r2head=ListNode(head.next.val)
            r2head.next=rhead
            rhead=r2head
            head=head.next
        return rhead
            
