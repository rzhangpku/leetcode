# -*- coding:utf-8 -*-


#
# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once. 
#
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
#
#
# Example 2:
#
# Input: [3,3,7,7,10,11,11]
# Output: 10
#
#
#
# Note:
# Your solution should run in O(log n) time and O(1) space.
#
#


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        for i in xrange(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
