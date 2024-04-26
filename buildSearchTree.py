from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return None
        root = TreeNode(nums[nums_len // 2])
        root.left = self.sortedArrayToBST(nums[:nums_len // 2])
        root.right = self.sortedArrayToBST(nums[nums_len // 2 + 1:])

        return root.val

    
print(Solution().sortedArrayToBST([-10,-3,0,5,9,10,11,12,13,14,15,16]))

    
# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.