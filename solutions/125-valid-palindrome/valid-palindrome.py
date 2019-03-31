# -*- coding:utf-8 -*-


# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s=re.sub('[^0-9a-zA-Z]',"",s)
        s=s.lower()
        if s[::-1]==s:
            return True
        else:
            return False
