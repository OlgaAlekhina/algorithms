# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def path_sum(self, root, target_sum):
        stack = []
        visited = []
        path_sum = 0
        while root:
            stack.append(root)
            path_sum += root.val
            root = root.left
        while stack:
            root = stack.pop()
            if root in visited:
                path_sum -= root.val
                continue
            if not root.left and not root.right:
                if path_sum == target_sum:
                    return True
                path_sum -= root.val
            elif root.right:
                visited.append(root)
                stack.append(root)
                root = root.right
                while root:
                    stack.append(root)
                    path_sum += root.val
                    root = root.left
            else: 
                path_sum -= root.val
                
        return False


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
print(s.path_sum(n1, 2))
                
                

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.