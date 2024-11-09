from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_nodes(node):
            if not node:
                return []
            return get_nodes(node.left) + [node.val] + get_nodes(node.right)

        nodes_list = get_nodes(root)
        res = nodes_list[1] - nodes_list[0]
        for i in range(2, len(nodes_list)):
            res = min(res, nodes_list[i] - nodes_list[i - 1])

        return res


# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105