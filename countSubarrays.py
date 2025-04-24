from typing import List


def count_subarrays(nums: List[int]) -> int:
    distinct_elements, elem_dict, res, nums_len = set(nums), {}, 0, len(nums)
    elem_number = len(distinct_elements)
    for num in distinct_elements:
        elem_dict[num] = 0
    distinct_elements = {nums[0]} if elem_number > 1 else set()
    elem_dict[nums[0]] = 1 if elem_number > 1 else 0
    i, j = (0, 0) if elem_number > 1 else (-1, -1)
    while i <= j:
        if len(distinct_elements) == elem_number:
            res += nums_len - j
            i += 1
            if elem_dict[nums[i - 1]] == 1:
                distinct_elements.remove(nums[i - 1])
            elem_dict[nums[i - 1]] -= 1 if elem_dict[nums[i - 1]] > 0 else 0
        else:
            j += 1 if j < nums_len else 0
            if j == nums_len:
                break
            elem_dict[nums[j]] += 1
            distinct_elements.add(nums[j])
            
    return res


print(count_subarrays([5,5,5,5,5,5]))

# You are given an array nums consisting of positive integers.
#
# We call a subarray of an array complete if the following condition is satisfied:
#
# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
#
# A subarray is a contiguous non-empty part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
# Example 2:
#
# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000