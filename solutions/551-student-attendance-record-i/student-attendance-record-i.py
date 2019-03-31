# -*- coding:utf-8 -*-


# You are given a string representing an attendance record for a student. The record only contains the following three characters:
#
#
#
# 'A' : Absent. 
# 'L' : Late.
#  'P' : Present. 
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).    
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#
#
#
#
#


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=0
        n=len(s)
        for i in xrange(n):
            if s[i]=="A":
                a+=1
            elif s[i]=="L":
                if i+1<n and i+2<n:
                    if s[i+1]=="L" and s[i+2]=="L":
                        return False
        if a<=1:
            return True
        else:
            return False
