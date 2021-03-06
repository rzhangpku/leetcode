# -*- coding:utf-8 -*-


# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution(object):
    def getNext(self, row):
        r=[1]
        for i in xrange(len(row)-1):
            r.append(row[i]+row[i+1])
        r.append(1)
        return r
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        else:
            r=[1,1]
            for i in xrange(rowIndex-1):
                r=Solution.getNext(self, r)
        return r
