# -*- coding:utf-8 -*-


# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
#
#
# 	Each group has exactly X cards.
# 	All the cards in each group have the same integer.
#
#
#  
#
# Example 1:
#
#
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 3:
#
#
# Input: [1]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 4:
#
#
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
#
#
#
# Example 5:
#
#
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
#
#
#
#
#
#
#
# Note:
#
#
# 	1 <= deck.length <= 10000
# 	0 <= deck[i] < 10000
#
#
#
#
#
#
#  
#
#
#
#
#


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        deck_dict={}
        for i in deck:
            if i in deck_dict:
                deck_dict[i]+=1
            else:
                deck_dict[i]=1
        vals_list=deck_dict.values()
        min_val=min(vals_list)
        for i in range(min_val,0,-1):
            flag=1
            for j in vals_list:
                if j%i!=0:
                    flag=0
                    break
            if flag==1:
                com_divisor=i
                break
        if com_divisor>1:
            return True
        else:
            return False
