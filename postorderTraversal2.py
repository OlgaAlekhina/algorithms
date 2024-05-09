# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root):
        if not root:
            return []
        traversal = []
        stack = [root]
        visited = []
        while stack:
            root = stack.pop()
            if root.left and root.left not in visited:
                while root:
                    stack.append(root)
                    root = root.left
                continue
            if root.right and root.right not in visited:
                stack.append(root)
                root = root.right
                stack.append(root)
                continue
            else:
                traversal.append(root.val)
                visited.append(root)

        return traversal
    
    
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
print(s.postorder_traversal(n1))
    
# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?