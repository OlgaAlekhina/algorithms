# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traversal(self, root):
        if not root:
            return []
        node_list = [root.val]
        cur_node = root
        stack = [root] if root.right else []
        while cur_node.left:
            cur_node = cur_node.left
            node_list.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node)
        while stack:
            cur_node = stack.pop()
            cur_node = cur_node.right
            node_list.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node)
            while cur_node.left:
                cur_node = cur_node.left
                node_list.append(cur_node.val)
                if cur_node.right:
                    stack.append(cur_node)

        return node_list
    
    
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
print(s.preorder_traversal(n1))
