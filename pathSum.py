# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def path_sum(self, root, target_sum):
        if not root:
            return False
            
        if not root.right and not root.left:
            return root.val == target_sum
            
        left_path = self.path_sum(root.left, target_sum - root.val)
        right_path = self.path_sum(root.right, target_sum - root.val)
        
        return left_path or right_path
    
    
    
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
print(s.path_sum(n1, 7))
    
    
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.