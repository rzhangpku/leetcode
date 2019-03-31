# -*- coding:utf-8 -*-


# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.r=0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.r=0
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 0
        if root.left!=None and root.left.left==None and root.left.right==None:
            self.r+=root.left.val
        if root.left!=None:
            self.r+=Solution.sumOfLeftLeaves(self, root.left)
        if root.right!=None:
            self.r+=Solution.sumOfLeftLeaves(self, root.right)
        return self.r
