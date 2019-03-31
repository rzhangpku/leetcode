# -*- coding:utf-8 -*-


# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        else:
            l=len(nums)
            if l==1:
                return [0,0]
            for i in range(l):
                if i==0:
                    if nums[i]==target:
                        r1=i
                else:
                    if nums[i]==target and nums[i-1]!=target:
                        r1=i
                if i==l-1:
                    if nums[i]==target:
                        r2=i
                else:
                    if nums[i]==target and nums[i+1]!=target:
                        r2=i
            return [r1,r2]
