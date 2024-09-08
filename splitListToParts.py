from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        len_list = 0
        cur = head
        res = []
        while cur:
            len_list += 1
            cur = cur.next
        len_parts = len_list // k
        extra_len = len_list % k
        while k:
            count = len_parts + 1 if extra_len > 0 else len_parts
            new_head = head
            res.append(new_head)
            while count > 1:
                if new_head:
                    new_head = new_head.next
                count -= 1
            k -= 1
            extra_len -= 1
            head = new_head.next if new_head else None
            if new_head:
                new_head.next = None

        return res


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n4 = ListNode(4)
n2.next = n3
n5 = ListNode(5)
# n3.next = n4
# n6 = ListNode(6)
# n4.next = n5
# n5.next = n6
s = Solution()

print(s.splitListToParts(n1, 5))

# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
#
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
#
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
#
# Return an array of the k parts.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50