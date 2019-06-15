# -*- coding:utf-8 -*-


# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#  
#


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        sp=s.split(" ")
        r=len(sp[-1])
        i=-2
        while r==0:
            try:
                r=len(sp[i])
            except:
                return 0
            i-=1
        return r
