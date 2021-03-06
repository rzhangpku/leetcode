# -*- coding:utf-8 -*-


#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l==1:
            return 0
        for i in range(l):
            if s[i] not in s[i+1:]+s[:i]:
                return i
        return -1
