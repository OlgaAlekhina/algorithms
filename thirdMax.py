from typing import List


def third_max(nums: List[int]) -> int:
    m1, m2, m3 = nums[0], None, None
    for num in nums:
        if num in (m1, m2, m3):
            continue
        if num > m1:
            m1, m2, m3 = num, m1, m2
        elif m2 is not None and num > m2:
            m2, m3 = num, m2
        elif m2 is None:
            m2 = num
        elif (m3 is not None and num > m3) or m3 is None:
            m3 = num

    return m3 if m3 is not None else m1


print(third_max([3,2,1,6,3,-7,0]))

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
#
#
#
# Example 1:
#
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:
#
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
#
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
# Follow up: Can you find an O(n) solution?