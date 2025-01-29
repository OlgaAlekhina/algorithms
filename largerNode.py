# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res, nodes_stack, count = [], [], 0
        while head.next:
            if head.next.val > head.val:
                res.append(head.next.val)
                while nodes_stack and head.next.val > nodes_stack[-1][0]:
                    node = nodes_stack.pop()
                    res[node[1]] = head.next.val
            else:
                nodes_stack.append((head.val, count))
                res.append(0)
            head = head.next
            count += 1
        res.append(0)

        return res




# You are given the head of a linked list with n nodes.
#
# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
#
# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
#
#
#
# Example 1:
#
#
# Input: head = [2,1,5]
# Output: [5,5,0]
# Example 2:
#
#
# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= n <= 104
# 1 <= Node.val <= 109