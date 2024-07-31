from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        nodes_list = []
        while head:
            nodes_list.append(head.val)
            head = head.next

        return nodes_list == nodes_list[::-1]


n1 = ListNode(5)
n2 = ListNode(1)
n3 = ListNode(5)
n1.next = n2
n4 = ListNode(5)
n2.next = n3
n5 = ListNode(7)
# n3.next = n4
# n6 = ListNode(10)
# n4.next = n5
# n5.next = n6
s = Solution()

print(s.is_palindrome(n1))

# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
#
#
# Follow up: Could you do it in O(n) time and O(1) space?