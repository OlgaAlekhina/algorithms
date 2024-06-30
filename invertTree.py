# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root):
        cur = root
        if not cur:
            return
        cur.left, cur.right = cur.right, cur.left
        self.invert_tree(cur.left)
        self.invert_tree(cur.right)
        return root


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
print(s.invert_tree(n1))

# Given the root of a binary tree, invert the tree, and return its root.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100