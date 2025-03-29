from typing import List
from collections import Counter


def number_pairs(nums: List[int]) -> int:
    def comb(n):
        if n == 1:
            return 0
        return comb(n - 1) + n - 1
    nums_dict, res = Counter(nums), 0
    for val in nums_dict.values():
        res += comb(val)

    return res


print(number_pairs([1,2,3]))

# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100