from typing import List
from collections import Counter


def find_unique(arr: List[int], k: int) -> int:
    nums_dict = Counter(arr)
    freq = list(nums_dict.values())
    freq.sort()
    res = len(freq)
    for num in freq:
        if (num - k) <= 0:
            res -= 1
            k -= num
        else:
            break
            
    return res


print(find_unique(arr = [5,5,4], k = 1))

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
#
#
#
# Example 1:
#
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length