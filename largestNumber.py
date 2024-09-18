from typing import List


def largest_number(nums: List[int]) -> str:
    str_list = list(map(str, nums))
    str_list.sort(key=lambda s: s * 10, reverse=True)
    res = ''.join(str_list)

    return res if int(res) > 0 else '0'


print(largest_number([432,43243]))

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
#
#
#
# Example 1:
#
# Input: nums = [10,2]
# Output: "210"
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

# https://leetcode.com/problems/largest-number/description/