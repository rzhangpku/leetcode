# -*- coding:utf-8 -*-


# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
#  
#
# Example 1:
#
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#
#  
#
# Note:
#
#
# 	2 <= A.length <= 20000
# 	A.length % 2 == 0
# 	0 <= A[i] <= 1000
#
#
#
#  
#


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a_even=[]
        a_odd=[]
        r=[]
        for a in A:
            if a%2==0:
                a_even.append(a)
            else:
                a_odd.append(a)
        l=len(A)
        for i in range(l/2):
            r.append(a_even[i])
            r.append(a_odd[i])
        return r
