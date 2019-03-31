# -*- coding:utf-8 -*-


# Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
#
# Return the largest possible sum of the array after modifying it in this way.
#
#  
#
# Example 1:
#
#
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
#
#
#
# Example 2:
#
#
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
#
#
#
# Example 3:
#
#
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
#
#
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 10000
# 	1 <= K <= 10000
# 	-100 <= A[i] <= 100
#
#


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s=0
        A=sorted(A)
        for a in A:
            if a<0 and K>0:
                s-=a
                K-=1
            else:
                s+=a
        if K>0:
            if K%2==0:
                return s
            else:
                s=s-2*min([a if a>0 else -a for a in A])
                return s
        else:
            return s
