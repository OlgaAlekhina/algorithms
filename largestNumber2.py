from typing import List
from functools import cmp_to_key


def largest_number(nums: List[int]) -> str:
    def cmp_str(a, b):
        if a + b > b + a:
            return 1
        elif a+ b < b + a:
            return -1
        else: return 0

    str_list = list(map(str, nums))
    str_list.sort(key=cmp_to_key(cmp_str), reverse=True)

    return ''.join(str_list) if str_list[0] != '0' else '0'


print(largest_number([342,3423]))

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