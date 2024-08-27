from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_list, count = 0, 0
        node = head
        while node:
            len_list += 1
            node = node.next
        node = head
        while count < len_list // 2:
            node = node.next
            count += 1

        return node


n1 = ListNode(3)

print(Solution().middleNode(n1))

# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100