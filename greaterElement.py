from typing import List


def greater_element(nums: List[int]) -> List[int]:
    res = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            res[i] = nums[i + 1]
            while stack:
                if stack[-1][0] < nums[i + 1]:
                    res[stack[-1][1]] = nums[i + 1]
                    stack.pop()
                else:
                    break
        else:
            stack.append((nums[i], i))
    stack.append((nums[-1], len(nums) - 1))
    for i in range(len(nums)):
        if len(stack) == 1:
            res[stack[0][1]] = -1
            return res
        while stack:
            if stack[-1][0] < nums[i]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
            else:
                break

    return res


print(greater_element([1,2,2,2,2,2,2,2,2,2,2,2]))

# https://leetcode.com/problems/next-greater-element-ii/description/
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
#
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:
#
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109