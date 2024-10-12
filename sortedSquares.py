from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    res, pos_ind = [], None
    for ind, val in enumerate(nums):
        if val >= 0:
            pos_ind = ind
            break
    neg_ind = pos_ind - 1 if pos_ind is not None else len(nums) - 1
    pos_ind = len(nums) if pos_ind is None else pos_ind
    while pos_ind < len(nums) and neg_ind >= 0:
        if nums[pos_ind] < abs(nums[neg_ind]):
            res.append(nums[pos_ind] ** 2)
            pos_ind += 1
        elif nums[pos_ind] > abs(nums[neg_ind]):
            res.append(nums[neg_ind] ** 2)
            neg_ind -= 1
        else:
            res += [nums[neg_ind] ** 2] * 2
            pos_ind += 1
            neg_ind -= 1
    if pos_ind < len(nums):
        for num in nums[pos_ind:]:
            res.append(num ** 2)
    if neg_ind >= 0:
        for num in nums[neg_ind::-1]:
            res.append(num ** 2)

    return res


print(sorted_squares([-7,-5,-3]))

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
#
#
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?