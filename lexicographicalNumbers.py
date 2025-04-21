from typing import List
import heapq


def lexicographical_numbers(n: int) -> List[int]:
    str_heap, res = [], [0] * n
    for num in range(1, n + 1):
        heapq.heappush(str_heap, str(num))
    for i in range(1, n + 1):
        res[i - 1] = int(heapq.heappop(str_heap))

    return res


print(lexicographical_numbers(13))

# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.
#
#
#
# Example 1:
#
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
#
# Input: n = 2
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= n <= 5 * 104