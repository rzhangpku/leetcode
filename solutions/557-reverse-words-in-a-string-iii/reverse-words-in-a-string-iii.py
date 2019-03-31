# -*- coding:utf-8 -*-


# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
#
#
# Note:
# In the string, each word is separated by single space and there will not be any extra space in the string.
#


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl=[]
        for word in s.split(' '):
            wordl=[]
            for i in xrange(len(word)-1,-1,-1):
                wordl.append(word[i])
            sl.append(''.join(wordl))
        rs=' '.join(sl)
        return rs
