from typing import List


def longest_subarray(nums: List[int]) -> int:
    count1, count2, zero_count, res, zero_flag = 0, 0, 0, 0, False
    for num in nums:
        if num == 0:
            zero_count += 1
            if zero_count == 1:
                res = max(res, count1 + count2) if zero_flag else max(res, count2)
                count1 = count2
                count2 = 0
                zero_flag = True
            else:
                zero_flag = False           
        else:
            zero_count = 0
            count2 += 1
    res = max(res, count1 + count2) if zero_flag else max(res, count2)

    return res if count2 < len(nums) else res - 1


print(longest_subarray([1,1,1]))

# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.