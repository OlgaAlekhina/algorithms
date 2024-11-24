from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        while root:
            if root.left and not root.right:
                root = root.left
            elif root.right and not root.left:
                root = root.right
            elif root.left and root.right:
                root = root.left if height(root.left) >= height(root.right) else root.right
            else:
                return root.val


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
print(s.findBottomLeftValue(n1))

# Given the root of a binary tree, return the leftmost value in the last row of the tree.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
# Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1