# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
    
    
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(5)
n5 = TreeNode(1)
n6 = TreeNode(12)
n7 = TreeNode(6)
n8 = TreeNode(10)
n1.right = n2
n1.left = n3
n2.right = n4
n2.left = n5
n3.left = n6
n3.right = n7
n7.left = n8

s = Solution()
print(s.max_depth(n1))
    
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.