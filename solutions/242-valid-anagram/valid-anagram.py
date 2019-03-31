# -*- coding:utf-8 -*-


# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#


class Solution(object):
    def getDict(self, s):
        dic={}
        for i in s:
            try:
                dic[i]+=1
            except:
                dic[i]=1
        return dic
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl=len(s)
        tl=len(t)
        if sl!=tl:
            return False
        else:
            if set(s)!=set(t):
                return False
            else:
                if Solution.getDict(self, s)!=Solution.getDict(self, t):
                    return False
                else:
                    return True
