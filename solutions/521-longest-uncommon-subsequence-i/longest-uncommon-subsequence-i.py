# -*- coding:utf-8 -*-


#
# Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
#
#
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
#
#
#
# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
#
#
# Example 1:
#
# Input: "aba", "cdc"
# Output: 3
# Explanation: The longest uncommon subsequence is "aba" (or "cdc"), because "aba" is a subsequence of "aba", but not a subsequence of any other strings in the group of two strings. 
#
#
#
# Note:
#
# Both strings' lengths will not exceed 100.
# Only letters from a ~ z will appear in input strings. 
#
#


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        la=len(a)
        lb=len(b)
        ml=-1
        for i in xrange(la):
            for j in xrange(i+1,la+1):
                if a[i:j] not in b:
                    l=len(a[i:j])
                    if l>ml:
                        ms=a[i:j]
                        ml=l
        for i in xrange(lb):
            for j in xrange(i+1,lb+1):
                if b[i:j] not in a:
                    l=len(b[i:j])
                    if l>ml:
                        ms=b[i:j]
                        ml=l
        return ml
