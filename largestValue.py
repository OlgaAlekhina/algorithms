from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        res = []
        while q:
            max_val = q[0].val
            len_row = len(q)
            while len_row:
                node = q.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                len_row -= 1
            res.append(max_val)
            
        return res
        
        
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
n1.right = n2
n1.left = n3
n3.right = n4
n3.left = n5
n4.right = n6
n6.right = n7
n5.right = n9
n5.left = n8
n9.right = n10
n10.left = n11
n10.right = n12
n12.right = n13
s = Solution()
print(s.largestValues(n1))            


# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
#
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:
#
# Input: root = [1,2,3]
# Output: [1,3]
#
#
# Constraints:
#
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1