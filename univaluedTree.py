from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                if cur.left.val != root.val:
                    return False
                stack.append(cur.left)
            if cur.right:
                if cur.right.val != root.val:
                    return False
                stack.append(cur.right)

        return True


# A binary tree is uni-valued if every node in the tree has the same value.
#
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:
#
#
# Input: root = [2,2,2,5,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100