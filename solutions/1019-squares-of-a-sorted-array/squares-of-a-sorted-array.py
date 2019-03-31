# -*- coding:utf-8 -*-


# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
#  
#
#
# Example 1:
#
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
#
#
# Example 2:
#
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 10000
# 	-10000 <= A[i] <= 10000
# 	A is sorted in non-decreasing order.
#
#
#


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares_a=list()
        for a in A:
            squares_a.append(pow(a,2))
        squares_a_sorted=sorted(squares_a)
        return squares_a_sorted
