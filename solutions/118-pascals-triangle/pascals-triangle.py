# -*- coding:utf-8 -*-


# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution(object):
    def getNext(self, row):
        r=[1]
        for i in xrange(len(row)-1):
            r.append(row[i]+row[i+1])
        r.append(1)
        return r
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        else:
            r=[[1],[1,1]]
            for i in xrange(2,numRows):
                r.append(Solution.getNext(self, r[-1]))
        return r
