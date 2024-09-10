from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def max_common_div(n1, n2):
            rem1 = max(n1, n2) % min(n1, n2)
            if rem1 == 0:
                return min(n1, n2)
            rem2 = min(n1, n2) % rem1
            if rem2 == 0:
                return rem1
            while rem1 % rem2 != 0:
                rem1, rem2 = rem2, rem1 % rem2

            return rem2

        cur = head
        while cur.next:
            next_node = cur.next
            div = max_common_div(cur.val, cur.next.val)
            cur.next = ListNode(div)
            cur.next.next = next_node
            cur = next_node

        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur.val)
        #     cur = cur.next
        # print(nodes)

        return head


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

print(s.insertGreatestCommonDivisors(n1))

# Given the head of a linked list head, in which each node contains an integer value.
#
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
#
# Return the linked list after insertion.
#
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
#
#
#
# Example 1:
#
#
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.
# Example 2:
#
#
# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5000].
# 1 <= Node.val <= 1000