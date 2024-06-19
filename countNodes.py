from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_nodes(root):
    nodes, height = 0, 0
    while root:
        nodes += 2 ** height
        height += 1
        root = root.left

    return nodes


class Solution:
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        nodes = 0
        while root:
            nodes += 1
            m1 = max_nodes(root.left)
            m2 = max_nodes(root.right)
            if m1 > m2:
                nodes += m2
                root = root.left
            else:
                nodes += m1
                root = root.right

        return nodes


n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(5)
n5 = TreeNode(1)
n6 = TreeNode(12)
n7 = TreeNode(6)
n8 = TreeNode(10)
n9 = TreeNode(10)
n10 = TreeNode(10)
n1.right = n2
n1.left = n3
n2.right = n4
n2.left = n5
n3.left = n6
n3.right = n7
n6.left = n8
n6.right = n9
n7.left = n10

s = Solution()
print(s.count_nodes(n1))

# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:
#
# Input: root = []
# Output: 0
# Example 3:
#
# Input: root = [1]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.