from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def preorder_traversal(root, trav):
            if not root:
                return
            preorder_traversal(root.left, trav)
            if len(trav) == 0 or trav[-1][0] != root.val:
                trav.append([root.val, 1])
            else:
                trav[-1][1] += 1
            preorder_traversal(root.right, trav)
            return trav

        trav = preorder_traversal(root, [])
        trav.sort(key=lambda x: x[1], reverse=True)
        mode_freq = trav[0][1]
        res = []
        for item in trav:
            if item[1] == mode_freq:
                res.append(item[0])
            else:
                break

        return res


n1 = TreeNode(10)
n2 = TreeNode(12)
n3 = TreeNode(9)
n4 = TreeNode(9)
n5 = TreeNode(8)
n6 = TreeNode(7)
n7 = TreeNode(8)
n8 = TreeNode(6)
n1.right = n2
n1.left = n3
n3.right = n4
n3.left = n5
n5.left = n6
n5.right = n7
n6.left = n8

s = Solution()
print(s.findMode(n1))

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
#
# If the tree has more than one mode, return them in any order.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:
#
# Input: root = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
#
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).