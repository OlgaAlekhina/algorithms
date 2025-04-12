from typing import List
from collections import Counter


def frequent_elements(nums: List[int], k: int) -> List[int]:
    freq_dict, res = Counter(nums), []
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for freq in sorted_freq:
        res.append(freq[0])
        k -= 1
        if k == 0:
            return res


print(frequent_elements(nums = [1,1,1,2,2,3,3,3,3,3,3], k = 2))

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.