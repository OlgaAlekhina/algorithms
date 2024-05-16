# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluate_tree(self, root) -> bool:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        if root.val == 2:
            return self.evaluate_tree(root.left) or self.evaluate_tree(root.right)
        if root.val == 3:
            return self.evaluate_tree(root.left) and self.evaluate_tree(root.right)
    
    
n1 = TreeNode(3)
n2 = TreeNode(3)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(0)
n6 = TreeNode(12)
n7 = TreeNode(6)
n8 = TreeNode(10)
n1.right = n2
n1.left = n3
n2.right = n4
n2.left = n5
# n3.left = n6
# n3.right = n7
# n7.left = n8

s = Solution()
print(s.evaluate_tree(n1))
    
    
# You are given the root of a full binary tree with the following properties:
#
# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:
#
# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.
#
# A full binary tree is a binary tree where each node has either 0 or 2 children.
#
# A leaf node is a node that has zero children.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3,null,null,0,1]
# Output: true
# Explanation: The above diagram illustrates the evaluation process.
# The AND node evaluates to False AND True = False.
# The OR node evaluates to True OR False = True.
# The root node evaluates to True, so we return true.
# Example 2:
#
# Input: root = [0]
# Output: false
# Explanation: The root node is a leaf node and it evaluates to false, so we return false.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 3
# Every node has either 0 or 2 children.
# Leaf nodes have a value of 0 or 1.
# Non-leaf nodes have a value of 2 or 3.