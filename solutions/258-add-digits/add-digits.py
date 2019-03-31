# -*- coding:utf-8 -*-


# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution(object):
    def bit(self, num):
        bit_n=[]
        while num!=0:
            bit_n.append(num%10)
            num=num/10
        return bit_n
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit_n=Solution.bit(self, num)
        while sum(bit_n)>=10:
            bit_n=Solution.bit(self, sum(bit_n))
        return sum(bit_n)
