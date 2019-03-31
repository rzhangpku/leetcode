# -*- coding:utf-8 -*-


# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
#
# Input: 2.00000, 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: 2.10000, 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#
# Note:
#
#
# 	-100.0 < x < 100.0
# 	n is a 32-bit signed integer, within the range [−231, 231 − 1]
#
#


#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.63%)
# Total Accepted:    296.1K
# Total Submissions: 1.1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        if n==2:
            return x*x
        if n<0:
            return 1/Solution.myPow(self, x, -n)
        if n%2==0:
            tmp=Solution.myPow(self, x, n/2)
            return tmp*tmp
        else:
            tmp1=Solution.myPow(self, x, n/2)
            tmp2=Solution.myPow(self, x, n/2+1)
            return tmp1*tmp2
        


