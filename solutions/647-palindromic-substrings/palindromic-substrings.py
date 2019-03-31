# -*- coding:utf-8 -*-


# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
#
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#  
#
# Example 2:
#
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#  
#
# Note:
#
#
# 	The input string length won't exceed 1000.
#
#
#  
#


class Solution(object):
    def countStartOne(self, s):
        r=0
        for i in xrange(len(s)):
            t=s[:i+1]
            if t==t[::-1]:
                r+=1
        return r
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        l=len(s)
        for i in xrange(l):
            t1=s[i:]
            r+=Solution.countStartOne(self, t1)
        return r
