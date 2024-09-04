from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = head
        cur2 = head.next if cur1 else None
        cur3 = cur2.next if cur2 else None
        while cur3:
            cur2.next = cur3.next
            cur2 = cur3.next
            cur3.next = cur1.next
            cur1.next = cur3
            cur1 = cur3
            cur3 = cur2.next if cur2 else None

        # cur = head
        # nodes = []
        # while cur:
        #     nodes.append(cur.val)
        #     cur = cur.next
        # print(nodes)

        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
# n1.next = n2
n4 = ListNode(4)
# n2.next = n3
n5 = ListNode(5)
# n3.next = n4
n6 = ListNode(6)
# n4.next = n5
# n5.next = n6
s = Solution()

print(s.oddEvenList(n1))

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
# Constraints:
#
# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106