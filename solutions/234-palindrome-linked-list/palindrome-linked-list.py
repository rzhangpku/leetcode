# -*- coding:utf-8 -*-


# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rhead=Solution.reverseList(self, head)
        while head!=None:
            if head.val!=rhead.val:
                return False
            else:
                head=head.next
                rhead=rhead.next
        return True

