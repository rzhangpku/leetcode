# -*- coding:utf-8 -*-


# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
#
#
# Input: 16
# Output: true
#
#
#
# Example 2:
#
#
# Input: 14
# Output: false
#
#
#


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqr=1
        while sqr**2<num:
            sqr+=1
        if sqr**2==num:
            return True
        else:
            return False
