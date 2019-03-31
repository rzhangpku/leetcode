# -*- coding:utf-8 -*-


# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
#
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
#
#
# Note:
#
#
# 	S will be a string with length between 1 and 12.
# 	S will consist only of letters or digits.
#
#


from itertools import combinations
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res=list()
        res.append(S)
        TS=list()
        l=len(S)
        flagl=list()
        for i in xrange(l):
            vi=S[i]
            oi=ord(vi)
            if oi>=65 and oi<=90:
                si=vi.lower()
                TS.append(si)
                flagl.append(i)
            elif oi>=97 and oi<=122:
                bi=vi.upper()
                TS.append(bi)
                flagl.append(i)
            else:
                TS.append(i)
        if flagl==[]:
            return res
        else:
            fl=len(flagl)
            for i in xrange(1,fl+1):
                comflags=list(combinations(flagl, i))
                for comflag in comflags:
                    rsi=S
                    for j in comflag:
                        rsi=rsi[:j]+TS[j]+rsi[j+1:]
                    res.append(rsi)
        return res
