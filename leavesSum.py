# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodes_queue = deque([root])
        while nodes_queue:
            row_sum = 0
            row_len = len(nodes_queue)
            for i in range(row_len):
                node = nodes_queue.popleft()
                row_sum += node.val
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)

        return row_sum



# Given the root of a binary tree, return the sum of values of its deepest leaves.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100