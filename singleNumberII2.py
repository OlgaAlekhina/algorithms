from typing import List


def single_number(nums: List) -> int:
    bits_list = [0] * 32
    for num in nums:
        count = 0
        if num < 0:
            num = num & (2**32 - 1)
        while num:
            if num & 1:
                bits_list[count] += 1
            count += 1
            num >>= 1
    res = ''
    for bit in bits_list:
        if bit % 3 == 0:
            res += '0'
        else:
            res += '1'
    res = int(res[::-1], 2)
    return res if res < 2**31 else res - 2**32


print(single_number([0,1,0,1,0,1,-99]))

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