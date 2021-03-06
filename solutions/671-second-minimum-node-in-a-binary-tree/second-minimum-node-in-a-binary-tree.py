# -*- coding:utf-8 -*-


# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
#
#
# Input: 
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#
#
#  
#
# Example 2:
#
#
# Input: 
#     2
#    / \
#   2   2
#
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
#
#
#  
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left!=None:
            if root.val==root.left.val and root.val==root.right.val:
                sl=Solution.findSecondMinimumValue(self, root.left)
                sr=Solution.findSecondMinimumValue(self, root.right)
                if sl==-1 and sr==-1:
                    return -1
                elif sl==-1:
                    return sr
                elif sr==-1:
                    return sl
                else:
                    return min(sl, sr)
            elif root.val==root.left.val:
                sl=Solution.findSecondMinimumValue(self, root.left)
                sr=root.right.val
                if sl!=-1:
                    return min(sr, sl)
                else:
                    return sr
            elif root.val==root.right.val:
                sr=Solution.findSecondMinimumValue(self, root.right)
                sl=root.left.val
                if sr!=-1:
                    return min(sl, sr)
                else:
                    return sl
            else:
                return min(root.left.val, root.right.val)
        else:
            return -1
