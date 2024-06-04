def single_number(nums):
    if len(nums) == 2:
        return nums
    xor_sum, num1, num2 = 0, 0, 0
    for num in nums:
        xor_sum ^= num
    i = 0
    while xor_sum & 1 == 0:
        i += 1
        xor_sum >>= 1
    for num in nums:
        if num >> i & 1 == 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


print(single_number([1,2,1,3,2,5,5,-2,-2,10,10,100]))

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
#
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:
#
# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.