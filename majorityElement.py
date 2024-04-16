from collections import defaultdict


def majority_element(nums):
    len_nums = len(nums)
    dict_nums = defaultdict(int)
    for num in nums:
        dict_nums[num] += 1
    for key, val in dict_nums.items():
        if val > len_nums / 2:
            return key


print(majority_element([2,2,1,1,1,2,2,3,3,3,3,3,3,3,3]))

# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109