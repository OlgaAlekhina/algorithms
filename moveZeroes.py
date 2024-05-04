def moveZeroes(nums) -> None:
    zero_count = 0
    nums_len = len(nums)
    for i in range(nums_len):
        if nums[i] == 0:
            zero_count += 1
            continue
        if zero_count != 0:
            nums[i - zero_count] = nums[i]
    for i in range(nums_len - zero_count, nums_len):
        nums[i] = 0
    print(nums)
        
print(moveZeroes([1,5,0,6,1,5,0,6]))
        
        
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
# Follow up: Could you minimize the total number of operations done?