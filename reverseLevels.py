from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node):
    if not node:
        return []
    return traverse(node.left) + [node.val] + traverse(node.right)


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d1 = deque([root])
        d2 = []
        count = 0
        while d1:
            for node in d1:
                if not node.left:
                    return root
                if count % 2 == 0:
                    d2.append(node.left)
                    d2.append(node.right)
                else:
                    d2.append(node.right)
                    d2.append(node.left)
            l = len(d1)
            while l:
                d = d1.popleft()
                d.left = d2.pop()
                d.right = d2.pop()
                d1.append(d.left)
                d1.append(d.right)
                l -= 1
            count += 1


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)
n12 = TreeNode(12)
n13 = TreeNode(13)
n14 = TreeNode(14)
n15 = TreeNode(15)
n1.right = n3
n1.left = n2
n2.right = n5
n2.left = n4
n3.right = n7
n3.left = n6
n4.right = n9
n4.left = n8
n5.right = n11
n5.left = n10
n6.right = n13
n6.left = n12
n7.right = n15
n7.left = n14
s = Solution()
print(s.reverseOddLevels(n1))

# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
#
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
#
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
#
# The level of a node is the number of edges along the path between it and the root node.
#
#
#
# Example 1:
#
#
# Input: root = [2,3,5,8,13,21,34]
# Output: [2,5,3,8,13,21,34]
# Explanation:
# The tree has only one odd level.
# The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
# Example 2:
#
#
# Input: root = [7,13,11]
# Output: [7,11,13]
# Explanation:
# The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
# Example 3:
#
# Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
# Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
# Explanation:
# The odd levels have non-zero values.
# The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
# The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 214].
# 0 <= Node.val <= 105
# root is a perfect binary tree.