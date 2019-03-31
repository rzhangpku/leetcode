# -*- coding:utf-8 -*-


# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
#  
#
#
# Example 1:
#
#
# Input: "Hello"
# Output: "hello"
#
#
#
# Example 2:
#
#
# Input: "here"
# Output: "here"
#
#
#
# Example 3:
#
#
# Input: "LOVELY"
# Output: "lovely"
#
#
#
#
#


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        rlist=[]
        for i in str:
            li=i.lower()
            rlist.append(li)
        return "".join(rlist)
