from typing import List
from collections import Counter


def array_degree(nums: List[int]) -> int:
    nums_freq = Counter(nums)
    items =  sorted(nums_freq.items(), key=lambda x: x[1], reverse=True)
    degree = items[0][1]
    nums_set = {items[0][0]}
    for num, freq in items:
        if freq == degree:
            nums_set.add(num)
        else:
            break
    if len(nums) == len(nums_set):
        return 1
    deg_dict = {x: [None, None] for x in nums_set}
    for i, num in enumerate(nums):
        if num in deg_dict and deg_dict[num][0] is None:
            deg_dict[num][0] = i
    for i, num in enumerate(nums[::-1]):
        if num in deg_dict and deg_dict[num][1] is None:
            deg_dict[num][1] = len(nums) - i - 1
    res = 50001
    for arr in deg_dict.values():
        res = min(res, arr[1] - arr[0])

    return res + 1


print(array_degree([1,2,2,3,1]))

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
#
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
#
#
# Constraints:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.