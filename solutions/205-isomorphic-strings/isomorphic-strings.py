# -*- coding:utf-8 -*-


# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#


class Solution(object):
    def isIsomorphicTmp(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapDict={}
        for i in xrange(len(s)):
            try:
                if mapDict[s[i]]!=t[i]:
                    return False
            except:
                mapDict[s[i]]=t[i]
        return True
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Solution.isIsomorphicTmp(self, s, t) and Solution.isIsomorphicTmp(self, t, s)
                
