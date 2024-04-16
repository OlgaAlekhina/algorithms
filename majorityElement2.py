def majority_element(nums):
    len_nums = len(nums)
    nums.sort()
    count = 1
    i = 0
    while i < len_nums:
        while i < len_nums - 1 and nums[i + 1] == nums[i]:
            count += 1
            i += 1  
        if count > len_nums / 2 or i == len_nums - 1:
            return nums[i]
        i += 1
        count = 1


print(majority_element([6,6,6,6,6,6,2,2,2,2,2,2,2]))

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