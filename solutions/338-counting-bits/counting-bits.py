# -*- coding:utf-8 -*-


# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
#
# Follow up:
#
#
# 	It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# 	Space complexity should be O(n).
# 	Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
#


class Solution(object):
    def count1s(self, num):
        s=0
        dis=num/2
        rem=num%2
        while(dis!=0):
            if rem==1:
                s+=1
            num=dis
            dis=num/2
            rem=num%2
        if rem==1:
            s+=1
        return s
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r=[]
        for i in xrange(num+1):
            r.append(Solution.count1s(self, i))
        return r
