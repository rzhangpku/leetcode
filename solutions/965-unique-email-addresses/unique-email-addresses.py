# -*- coding:utf-8 -*-


# Every email consists of a local name and a domain name, separated by the @ sign.
#
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
#
# Besides lowercase letters, these emails may contain '.'s or '+'s.
#
# If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
#
# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
#
# It is possible to use both of these rules at the same time.
#
# Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
#
#  
#
#
# Example 1:
#
#
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
#
#
#  
#
# Note:
#
#
# 	1 <= emails[i].length <= 100
# 	1 <= emails.length <= 100
# 	Each emails[i] contains exactly one '@' character.
#
#
#


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_sets=set()
        for email in emails:
            names=email.split("@")
            local_name=names[0]
            domain_name=names[1]
            if "+" in local_name:
                local_name_re=local_name.split("+", 1)[0].replace(".", "")
            else:
                local_name_re=local_name.replace(".", "")
            email_re=local_name_re+"@"+domain_name
            email_sets.add(email_re)
        return len(email_sets)
        
