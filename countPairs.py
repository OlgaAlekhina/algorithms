from typing import List
from itertools import combinations


def count_pairs(nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    start, end, res = 0, len(nums) - 1, 0
    while start < end:
        if nums[start] + nums[end] > upper:
            end -= 1
        elif nums[start] + nums[end] < lower:
            start += 1
        else:
            break
    if start == end:
        return 0
    new_lower, new_upper = end, end
    for i in range(start, len(nums)):
        while nums[i] + nums[new_upper] > upper:
            new_upper -= 1
        new_upper += 1 if (nums[i] + nums[new_upper]) < lower else 0
        while new_lower > i and nums[i] + nums[new_lower] >= lower:
            new_lower -= 1
        new_lower += 1
        if new_upper < new_lower:
            break
        res += (new_upper - new_lower + 1) if lower <= (nums[i] + nums[new_upper]) <= upper else (new_upper - new_lower)

    return res


print(count_pairs([1,7,5,9,2,11], 12, 12))

# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
#
# A pair (i, j) is fair if:
#
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
#
#
# Example 1:
#
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:
#
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109