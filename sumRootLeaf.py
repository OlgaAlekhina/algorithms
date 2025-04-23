from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res_sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def help(node, dig_list, res_sum):
            if not node:
                return
            if not node.left and not node.right:
                dig_list.append(str(node.val))
                self.res_sum += int(''.join(dig_list))
                dig_list.pop()
                return
            dig_list.append(str(node.val))
            help(node.left, dig_list, res_sum)
            help(node.right, dig_list, res_sum)
            dig_list.pop()

        help(root, [], self.res_sum)
        return self.res_sum


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(1)
n11 = TreeNode(1)
n12 = TreeNode(2)
n13 = TreeNode(3)
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
print(s.sumNumbers(n1))


# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
#
#
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.