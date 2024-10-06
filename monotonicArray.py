from typing import List


def is_monotonic(nums: List[int]) -> bool:
    cur, more_flag = nums[0], None
    if nums[-1] > cur:
        more_flag = True
    elif nums[-1] < cur:
        more_flag = False
    for num in nums:
        if num > cur:
            if more_flag is False:
                return False
            if more_flag is None:
                more_flag = True
        elif num < cur:
            if more_flag is True:
                return False
            if more_flag is None:
                more_flag = False
        cur = num

    return True


print(is_monotonic([2]))

# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,3]
# Output: true
# Example 2:
#
# Input: nums = [6,5,4,4]
# Output: true
# Example 3:
#
# Input: nums = [1,3,2]
# Output: false
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105