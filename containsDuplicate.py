from collections import defaultdict


def contains_duplicate(nums, k: int) -> bool:
    nums_dict = defaultdict(list)
    for ind, val in enumerate(nums):
        nums_dict[val].append(ind)
    ind_list = list(filter(lambda x: len(x) > 1, nums_dict.values()))
    for i in ind_list:
        for j in range(len(i) - 1):
            if abs(i[j + 1] - i[j]) <= k:
                return True

    return False


print(contains_duplicate([1], 0))

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105