from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack, visited, res = [root], [], []
        while stack:
            if not stack[-1].left and not stack[-1].right:
                path = ''
                for node in stack:
                    path += f'{node.val}->'
                res.append(path[:-2])
                visited.append(stack.pop())
            elif stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
            elif stack[-1].right and stack[-1].right not in visited:
                stack.append(stack[-1].right)
            else:
                visited.append(stack.pop())

        return res


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n6.left = n7

print(Solution().binaryTreePaths(n1))

# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:
#
# Input: root = [1]
# Output: ["1"]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100