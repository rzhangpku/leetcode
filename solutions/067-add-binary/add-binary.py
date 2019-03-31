# -*- coding:utf-8 -*-


# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=="0" and b=="0":
            return "0"
        la=len(a)
        lb=len(b)
        tmp=0
        r=[]
        if la<lb:
            for i in xrange(-1, -1*(la+1), -1):
                s=int(a[i])+int(b[i])+tmp
                if s<2:
                    r.append(str(s))
                    tmp=0
                else:
                    r.append(str(s-2))
                    tmp=1
            for i in xrange(-1*(la+1), -1*(lb+1), -1):
                s=int(b[i])+tmp
                if s<2:
                    r.append(str(s))
                    tmp=0
                else:
                    r.append(str(s-2))
                    tmp=1
        elif la>lb:
            for i in xrange(-1, -1*(lb+1), -1):
                s=int(a[i])+int(b[i])+tmp
                if s<2:
                    r.append(str(s))
                    tmp=0
                else:
                    r.append(str(s-2))
                    tmp=1
            for i in xrange(-1*(lb+1), -1*(la+1), -1):
                print i
                s=int(a[i])+tmp
                if s<2:
                    r.append(str(s))
                    tmp=0
                else:
                    r.append(str(s-2))
                    tmp=1
        else:
            for i in xrange(lb-1, -1, -1):
                s=int(a[i])+int(b[i])+tmp
                if s<2:
                    r.append(str(s))
                    tmp=0
                else:
                    r.append(str(s-2))
                    tmp=1
        if tmp!=0:
            r.append(str(tmp))
        return "".join(r[::-1])
