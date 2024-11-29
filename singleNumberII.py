from typing import List


def single_number(nums: List) -> int:
    nums_dict, cur = {}, 0
    for i in range(len(nums) // 3 + 1):
        nums_dict[i] = 0
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            while nums_dict.get(cur) is None or nums_dict.get(cur) > 0:
                cur += 1
            nums_dict[num] = nums_dict.pop(cur)
            nums_dict[num] = 1
    for key, val in nums_dict.items():
        if val == 1:
            return key


print(single_number([0,1,0,1,0,1,99]))

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
#
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.