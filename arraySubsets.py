def subsets(nums):
    if not nums:
        return [[]]
    result = subsets(nums[:-1])
    return result + [s + [nums[-1]] for s in result]


print(subsets([1,2,3]))


# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.