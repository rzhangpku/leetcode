# -*- coding:utf-8 -*-


# Given two integers A and B, return any string S such that:
#
#
# 	S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# 	The substring 'aaa' does not occur in S;
# 	The substring 'bbb' does not occur in S.
#
#
#  
#
# Example 1:
#
#
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
#
#
#
# Example 2:
#
#
# Input: A = 4, B = 1
# Output: "aabaa"
#
#  
#
#
# Note:
#
#
# 	0 <= A <= 100
# 	0 <= B <= 100
# 	It is guaranteed such an S exists for the given A and B.
#
#


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        r=""
        if A>B:
            if A%2==0:
                for i in range(A/2):
                    r+="aa"
                    if B>0:
                        r+="b"
                        B-=1
                if B>0:
                    for i in range(B):
                        r=r[:2*(i+1)+i]+"b"+r[2*(i+1)+i:]
            else:
                for i in range(A/2):
                    r+="aa"
                    if B>0:
                        r+="b"
                        B-=1
                r+="a"
                if B>0:
                    for i in range(B):
                        r=r[:2*(i+1)+i]+"b"+r[2*(i+1)+i:]
        elif A==B:
            if A%2==0:
                for i in range(A/2):
                    r+="aa"
                    r+="bb"
            else:
                for i in range(A/2):
                    r+="aa"
                    r+="bb"
                r+="a"
                r+="b"
        else:
            if B%2==0:
                for i in range(B/2):
                    r+="bb"
                    if A>0:
                        r+="a"
                        A-=1
                if A>0:
                    for i in range(A):
                        r=r[:2*(i+1)+i]+"a"+r[2*(i+1)+i:]
            else:
                for i in range(B/2):
                    r+="bb"
                    if A>0:
                        r+="a"
                        A-=1
                r+="b"
                if A>0:
                    for i in range(A):
                        r=r[:2*(i+1)+i]+"a"+r[2*(i+1)+i:]
        return r
