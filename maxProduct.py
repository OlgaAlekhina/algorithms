from typing import List


def max_product(nums: List[int]) -> int:
    max1 = nums[0] if nums[0] >= nums[1] else nums[1]
    max2 = nums[0] if nums[0] < nums[1] else nums[1]
    for num in nums[2:]:
        if num > max1 and num > max2:
            max1, max2 = num, max1
        elif num == max1 or num > max2:
            max2 = num

    return (max1 - 1) * (max2 - 1)


print(max_product([1,5,4,5]))


# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
#
#
# Example 1:
#
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
# Example 2:
#
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
# Example 3:
#
# Input: nums = [3,7]
# Output: 12
#
#
# Constraints:
#
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3