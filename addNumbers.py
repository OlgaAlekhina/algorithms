from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node, first_number, second_number = l1, '', ''
        while node:
            first_number += str(node.val)
            node = node.next
        node = l2
        while node:
            second_number += str(node.val)
            node = node.next
        first_number, second_number = int(first_number), int(second_number)
        result_number = str(first_number + second_number)
        head = ListNode(int(result_number[0]))
        node = head
        for val in result_number[1:]:
            node.next = ListNode(int(val))
            node = node.next

        # print result number
        nodes_list = []
        node = head
        while node:
            nodes_list.append(node.val)
            node = node.next
        print('nodes_list: ', nodes_list)

        return head


n1 = ListNode(5)
n2 = ListNode(1)
n3 = ListNode(5)
n1.next = n2
n4 = ListNode(5)
n2.next = n3
n5 = ListNode(7)
n3.next = n4
n6 = ListNode(9)
n4.next = n5
n5.next = n6

n7 = ListNode(5)
n8 = ListNode(8)
n7.next = n8

s = Solution()
print(s.addTwoNumbers(n1, n7))


# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
#
#
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
#
#
# Follow up: Could you solve it without reversing the input lists?