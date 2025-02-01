from typing import List


def special_array(nums: List[int]) -> bool:
    if len(nums) == 0:
        return True
    last_bit1 = nums[0] & 1
    last_bit2 = nums[1] & 1
    if last_bit1 == last_bit2:
        return False
    for i in range(0, len(nums), 2):
        if nums[i] & 1 != last_bit1:
            return False
    for i in range(1, len(nums), 2):
        if nums[i] & 1 != last_bit2:
            return False

    return True


print(special_array([2,1,4,6]))

# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
#
#
#
# Example 1:
#
# Input: nums = [1]
#
# Output: true
#
# Explanation:
#
# There is only one element. So the answer is true.
#
# Example 2:
#
# Input: nums = [2,1,4]
#
# Output: true
#
# Explanation:
#
# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.
#
# Example 3:
#
# Input: nums = [4,3,1,6]
#
# Output: false
#
# Explanation:
#
# nums[1] and nums[2] are both odd. So the answer is false.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100