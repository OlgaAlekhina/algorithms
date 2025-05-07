from typing import List


def longest_subsequence(nums: List[int]) -> int:
    nums.sort()
    min_count, max_count, res, min_val = 0, 1, 0, nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            max_count += 1
        else:
            if nums[i - 1] - min_val == 1 and min_count:
                res = max(res, min_count + max_count)
            min_count, max_count, min_val = max_count, 1, nums[i - 1]
    if nums[len(nums) - 1] - min_val == 1 and min_count:
        res = max(res, min_count + max_count)

    return res


print(longest_subsequence([1,1,2,2]))

# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
#
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
#
#
#
# Example 1:
#
# Input: nums = [1,3,2,2,5,2,3,7]
#
# Output: 5
#
# Explanation:
#
# The longest harmonious subsequence is [3,2,2,2,3].
#
# Example 2:
#
# Input: nums = [1,2,3,4]
#
# Output: 2
#
# Explanation:
#
# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.
#
# Example 3:
#
# Input: nums = [1,1,1,1]
#
# Output: 0
#
# Explanation:
#
# No harmonic subsequence exists.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109