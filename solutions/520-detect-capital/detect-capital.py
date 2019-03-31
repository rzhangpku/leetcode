# -*- coding:utf-8 -*-


#
# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
#
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
#
#
# Example 1:
#
# Input: "USA"
# Output: True
#
#
#
# Example 2:
#
# Input: "FlaG"
# Output: False
#
#
#
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase latin letters.
#


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        lens=len(word)
        ind1=0
        ind2=0
        ind3=0
        for i in range(lens):
            if word[0].isupper():
                if i>0:
                    if word[i].isupper():
                        ind3=1
                    else:
                        ind1=1
            else:
                if i>0:
                    if word[i].isupper():
                        ind2=1
        if (ind1==1 and ind3==1) or ind2==1:
            return False
        else:
            return True
