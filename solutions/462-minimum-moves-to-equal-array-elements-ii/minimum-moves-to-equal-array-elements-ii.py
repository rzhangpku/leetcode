# -*- coding:utf-8 -*-


# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
#
# You may assume the array's length is at most 10,000.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 2
#
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=len(nums)
        if l%2!=0:
            cent=nums[(l-1)/2]
        else:
            cent=nums[l/2]
        return sum([abs(num-cent) for num in nums])
