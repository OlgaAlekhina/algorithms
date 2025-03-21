from typing import List
import heapq


def find_largest(nums: List[int], k: int) -> int:
    nums_heap = [-x for x in nums]
    heapq.heapify(nums_heap)
    for _ in range(k):
        res = -heapq.heappop(nums_heap)

    return res


print(find_largest(nums = [3,2,1,5,6,4], k = 2))

# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
#
#
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104