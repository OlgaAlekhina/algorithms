# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_balanced(self, root) -> bool:
        if not root:
            return True
        if abs(self.max_depth(root.left) - self.max_depth(root.right)) > 1:
            return False
        else:
            return self.is_balanced(root.left) and self.is_balanced(root.right)

    def max_depth(self, root):
        if not root:
            return 0
        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
        
        
        
        
# Given a binary tree, determine if it is height-balanced.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.