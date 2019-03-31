# -*- coding:utf-8 -*-


# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.
#
#  
#
# Example 1:
#
#
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
#
#
# Example 2:
#
#
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
#
#
# Example 3:
#
#
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
#
#  
#
# Note:  1 <= S.length <= 1000
#


#
# @lc app=leetcode id=830 lang=python
#
# [830] Positions of Large Groups
#
# https://leetcode.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (47.47%)
# Total Accepted:    23.2K
# Total Submissions: 48.9K
# Testcase Example:  '"abbxxxxzzy"'
#
# In a string S of lowercase letters, these letters form consecutive groups of
# the same character.
# 
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z" and "yy".
# 
# Call a group large if it has 3 or more characters.  We would like the
# starting and ending positions of every large group.
# 
# The final answer should be in lexicographic order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending
# positions 6.
# 
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# 
# 
# Example 3:
# 
# 
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# 
# 
# 
# Note:  1 <= S.length <= 1000
# 
#
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        r=[]
        l=len(S)
        count=1
        start=0
        for i in range(1,l):
            if S[i]==S[i-1]:
                count+=1
                if i==l-1 and count>=3:
                    end=i
                    r.append([start,end])
            else:
                if count>=3:
                    end=i-1
                    r.append([start,end])
                count=1
                start=i
        return r


