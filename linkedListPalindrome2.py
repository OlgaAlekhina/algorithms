from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        list_len = 0
        p = head
        while p:
            list_len += 1
            p = p.next
        mid = list_len // 2
        p1, p2 = None, head
        while mid > 0:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
            mid -= 1
        if list_len % 2 > 0:
            p2 = p2.next
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(3)
n1.next = n2
n4 = ListNode(3)
n2.next = n3
n5 = ListNode(1)
n3.next = n4
n6 = ListNode(0)
n4.next = n5
n5.next = n6
n7 = ListNode(0)
# n6.next = n7
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