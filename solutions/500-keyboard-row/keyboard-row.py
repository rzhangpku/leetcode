# -*- coding:utf-8 -*-


# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
#  
#
#
#  
#
# Example:
#
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#  
#
# Note:
#
#
# 	You may use one character in the keyboard more than once.
# 	You may assume the input string will only contain letters of alphabet.
#
#


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1=['q','w','e','r','t','y','u','i','o','p']
        row2=['a','s','d','f','g','h','j','k','l']
        row3=['z','x','c','v','b','n','m']
        output=[]
        for word in words:
            if word[0].lower() in row1:
                which_row=1
            elif word[0].lower() in row2:
                which_row=2
            else:
                which_row=3
            for char in word:
                if char.lower() in row1:
                    test_row=1
                elif char.lower() in row2:
                    test_row=2
                else:
                    test_row=3
                if test_row!=which_row:
                    break
            if test_row==which_row:
                output.append(word)
        return output
