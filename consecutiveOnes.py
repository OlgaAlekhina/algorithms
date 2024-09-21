from typing import List


def consecutive_ones(nums: List[int]) -> int:
    res, count = 0, 0
    for num in nums:
        if num == 1:
            count += 1
            res = count if count > res else res
        else:
            count = 0

    return res


print(consecutive_ones([0]))

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.