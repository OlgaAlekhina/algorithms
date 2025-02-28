from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0
    bit_list = []
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def help_func(root, bit_list):
            if not root:
                return
            bit_list.append(str(root.val))
            if not root.left and not root.right:
                self.res += int(''.join(bit_list), 2)
                bit_list.pop()
                return
            help_func(root.left, bit_list)
            help_func(root.right, bit_list)
            bit_list.pop()

        help_func(root, self.bit_list)
        return self.res


n1 = TreeNode(1)
n2 = TreeNode(0)
n3 = TreeNode(1)
n4 = TreeNode(0)
n5 = TreeNode(1)
n6 = TreeNode(0)
n7 = TreeNode(1)
n8 = TreeNode(1)
n9 = TreeNode(0)
n10 = TreeNode(0)
n11 = TreeNode(1)
n12 = TreeNode(1)
n13 = TreeNode(1)
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
print(s.sumRootToLeaf(n1))



# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
#
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.
#
#
#
# Example 1:
#
#
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:
#
# Input: root = [0]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.