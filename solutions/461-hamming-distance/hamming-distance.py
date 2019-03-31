# -*- coding:utf-8 -*-


# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#
#


class Solution(object):
    def bin(self, x):
        bin_x=[]
        while x!=0:
            rem=x%2
            x=x/2
            bin_x.append(rem)
        return bin_x
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x=Solution.bin(self, x)
        bin_y=Solution.bin(self, y)
        min_n=min(len(bin_x), len(bin_y))
        dist=0
        for i in range(min_n):
            if bin_x[i]!=bin_y[i]:
                dist+=1
        if len(bin_x) >= len(bin_y):
            for i in xrange(min_n, len(bin_x)):
                if bin_x[i]!=0:
                    dist+=1
        else:
            for i in xrange(min_n, len(bin_y)):
                if bin_y[i]!=0:
                    dist+=1
        return dist
