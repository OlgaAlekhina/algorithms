# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_elements(self, head, val: int):
        if not head:
            return
        if head.val == val:
            while head and head.val == val:
                head = head.next
        if not head:
            return
        cur = head
        while cur.next:
            if cur.next.val != val:
                cur = cur.next
            else:
                cur.next = cur.next.next

        # l = []
        # cur = head
        # while cur:
        #     l.append(cur.val)
        #     cur = cur.next
        # print('list', l)

        return head


n1 = ListNode(15)
n2 = ListNode(15)
n3 = ListNode(15)
n1.next = n2
n4 = ListNode(15)
n2.next = n3
n5 = ListNode(15)
n3.next = n4
n6 = ListNode(15)
n7 = ListNode(15)
n4.next = n5
n5.next = n6
n6.next = n7
s = Solution()

print(s.remove_elements(n1, 15))   
    
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:
#
# Input: head = [], val = 1
# Output: []
# Example 3:
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50