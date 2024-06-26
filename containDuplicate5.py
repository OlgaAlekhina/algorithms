def containsDuplicate(nums):
    while True:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return True
            elif nums[i + 1] < nums[i]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                count = 1
        if count == 0:
            break

    return False


print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109