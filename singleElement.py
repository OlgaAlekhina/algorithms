from typing import List


def single_element(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    start, end = 0, len(nums) - 1
    while end - start > 2:
        mid = (start + end) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        if nums[mid] == nums[mid - 1] and (mid - start) % 2 == 0:
            end = mid
        elif nums[mid] == nums[mid + 1] and (mid - start) % 2 != 0:
            end = mid - 1
        elif nums[mid] == nums[mid + 1] and (mid - start) % 2 == 0:
            start = mid
        else:
            start = mid + 1

    return nums[start] if nums[start] != nums[start + 1] else nums[end]


print(single_element([1,1,2,3,3,4,4,8,8,9,9,10,10]))

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105