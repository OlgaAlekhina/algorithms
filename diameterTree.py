from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    path = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_path(root):
            if not root:
                return 0
            return max(max_path(root.left), max_path(root.right)) + 1

        if not root:
            return
        res = max_path(root.left) + max_path(root.right) + 1
        self.path = max(res, self.path)
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.path


n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
n7 = TreeNode(5)
n8 = TreeNode(5)
n9 = TreeNode(6)
n10 = TreeNode(7)
n11 = TreeNode(8)
n12 = TreeNode(9)
n13 = TreeNode(10)
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
print(s.diameterOfBinaryTree(n1))

# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
#
# Input: root = [1,2]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100