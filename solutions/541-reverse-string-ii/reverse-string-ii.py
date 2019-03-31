# -*- coding:utf-8 -*-


#
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
#
#
# Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#
#
# Restrictions: 
#
#  The string consists of lower English letters only.
#  Length of the given string and k will in the range [1, 10000]
#


class Solution(object):
    def reverse(self, s):
        r=""
        for i in xrange(len(s)-1, -1, -1):
            r+=s[i]
        return r
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r=""
        n=len(s)
        k2=2*k
        for i in xrange(0,n,k2):
            r+=Solution.reverse(self, s[i: i+k])
            r+=s[i+k: i+k2]
        end=i+k2
        if (n-end)<k:
            r+=Solution.reverse(self, s[end: n])
        else:
            r+=Solution.reverse(self, s[end: end+k])
            r+=s[end+k: n]
        return r
