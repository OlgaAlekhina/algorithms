from typing import List


def monotonic_subarray(nums: list[int]) -> int:
    inc, max_len, count = False, 1, 1
    for i in range(len(nums) - 1):
        if (nums[i + 1] > nums[i]) and inc:
            count += 1
        elif (nums[i + 1] > nums[i]) and not inc:
            count = 2
            inc = True
        elif (nums[i + 1] < nums[i]) and inc:
            count = 2
            inc = False
        elif (nums[i + 1] < nums[i]) and not inc:
            count += 1
        else:
            count = 1
            inc = False
        max_len = max(max_len, count)

    return max_len


print(monotonic_subarray([1,4,3,3,2,5,6,7,2,3,10,20,19,18,3,6,7,23,5,7,3,5,6,12,45,4,5,2,1,9]))

# You are given an array of integers nums. Return the length of the longest
# subarray
#  of nums which is either
# strictly increasing
#  or
# strictly decreasing
# .
#
#
#
# Example 1:
#
# Input: nums = [1,4,3,3,2]
#
# Output: 2
#
# Explanation:
#
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
#
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
#
# Hence, we return 2.
#
# Example 2:
#
# Input: nums = [3,3,3,3]
#
# Output: 1
#
# Explanation:
#
# The strictly increasing subarrays of nums are [3], [3], [3], and [3].
#
# The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
#
# Hence, we return 1.
#
# Example 3:
#
# Input: nums = [3,2,1]
#
# Output: 3
#
# Explanation:
#
# The strictly increasing subarrays of nums are [3], [2], and [1].
#
# The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
#
# Hence, we return 3.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50