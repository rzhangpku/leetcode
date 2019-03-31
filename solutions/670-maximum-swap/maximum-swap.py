# -*- coding:utf-8 -*-


#
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
#
# Example 1:
#
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
#
# Example 2:
#
# Input: 9973
# Output: 9973
# Explanation: No swap.
#
#
#
#
# Note:
#
# The given number is in the range [0, 108]
#
#


class Solution(object):
    def maxValue(self, strs):
        strs_len=len(strs)
        maxv=-1
        for i in xrange(strs_len):
            v=int(strs[i])
            if maxv<=v:
                maxv=v
                maxi=i
        return maxv, maxi
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str=str(num)
        num_list=list(num_str)
        num_len=len(num_str)
        for i in xrange(num_len):
            if i == num_len-1:
                return num
            max_i,max_index=Solution.maxValue(self, num_str[i+1:])
            max_index=max_index+i+1
            if int(num_str[i])>=max_i:
                continue
            else:
                return int(num_str[:i]+num_str[max_index]+num_str[i+1:max_index]+num_str[i]+num_str[max_index+1:])
        return num
