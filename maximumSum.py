from typing import List
from collections import defaultdict


def max_sum(nums: List[int]) -> int:
    def dig_sum(num):
        res = 0
        while num:
            res += num % 10
            num //= 10

        return res

    nums_dict, res = defaultdict(list), -1
    for num in nums:
        d_sum = dig_sum(num)
        pair = nums_dict[d_sum]
        if len(pair) < 2:
            pair.append(num)
        else:
            min_ind = pair.index(min(pair))
            nums_dict[d_sum][min_ind] = max(num, min(pair))
    for pair in nums_dict.values():
        if len(pair) > 1:
            res = max(res, sum(pair))

    return res

        
print(max_sum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))

# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
#
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
#
#
#
# Example 1:
#
# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.
# Example 2:
#
# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109