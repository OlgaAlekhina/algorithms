from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodes_between_critical_points(self, head: Optional[ListNode]) -> List[int]:
        nodes_list = []
        count, min_len, max_len = 2, 100000, 0
        while head.next.next:
            if (head.next.val < head.val and head.next.val < head.next.next.val) or (head.next.val > head.val and head.next.val > head.next.next.val):
                if nodes_list:
                    dif = count - nodes_list[-1]
                    max_len += dif
                    min_len = dif if dif < min_len else min_len
                nodes_list.append(count)
            head = head.next
            count += 1
        if len(nodes_list) < 2:
            return [-1, -1]
        return [min_len, max_len]


n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(3)
n1.next = n2
n4 = ListNode(0)
n2.next = n3
n5 = ListNode(15)
n3.next = n4
n6 = ListNode(0)
n4.next = n5
n5.next = n6
s = Solution()

print(s.nodes_between_critical_points(n1))


# A critical point in a linked list is defined as either a local maxima or a local minima.
#
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
#
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
#
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
#
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
#
#
#
# Example 1:
#
#
# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].
# Example 2:
#
#
# Input: head = [5,3,1,2,5,1,2]
# Output: [1,3]
# Explanation: There are three critical points:
# - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
# - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
# - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
# The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
# The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
# Example 3:
#
#
# Input: head = [1,3,2,2,3,2,2,2,7]
# Output: [3,3]
# Explanation: There are two critical points:
# - [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
# - [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
# Both the minimum and maximum distances are between the second and the fifth node.
# Thus, minDistance and maxDistance is 5 - 2 = 3.
# Note that the last node is not considered a local maxima because it does not have a next node.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [2, 105].
# 1 <= Node.val <= 105