# -*- coding:utf-8 -*-


# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return 1+max(Solution.maxDepth(self, root.left), Solution.maxDepth(self, root.right))
