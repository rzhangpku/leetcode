# -*- coding:utf-8 -*-


# Let's call an array A a mountain if the following properties hold:
#
#
# 	A.length >= 3
# 	There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
#
#
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
# Example 1:
#
#
# Input: [0,1,0]
# Output: 1
#
#
#
# Example 2:
#
#
# Input: [0,2,1,0]
# Output: 1
#
#
# Note:
#
#
# 	3 <= A.length <= 10000
# 	0 <= A[i] <= 10^6
# 	A is a mountain, as defined above.
#
#


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        l=len(A)
        for i in range(1,l-1):
            if A[:i+1]==sorted(A[:i+1]) and A[i:]==sorted(A[i:], reverse=True):
                return i
        """
        r=False
        l=len(A)
        amax=max(A)
        for i in range(1,l-1):
            if A[i]==amax:
                return i
