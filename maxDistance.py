from typing import List


def max_distance(arrays: List[List[int]]) -> int:
    min_index = min(range(len(arrays)), key=lambda x: arrays[x][0])
    min_val = arrays[min_index][0]
    max_index = max(range(len(arrays)), key=lambda x: arrays[x][-1])
    max_val = arrays[max_index][-1]
    if min_index != max_index:
        return abs(max_val - min_val)
    max_index2 = max(range(len(arrays)), key=lambda x: arrays[x][-1] if x != min_index else -10000)
    max_val2 = arrays[max_index2][-1]
    min_index2 = min(range(len(arrays)), key=lambda x: arrays[x][0] if x != min_index else 10000)
    min_val2 = arrays[min_index2][0]

    return max(abs(max_val - min_val2), abs(max_val2 - min_val))


print(max_distance([[-1,1],[-3,1,4],[-2,-1,0,2]]))

# You are given m arrays, where each array is sorted in ascending order.
#
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
#
# Return the maximum distance.
#
#
#
# Example 1:
#
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Example 2:
#
# Input: arrays = [[1],[1]]
# Output: 0
#
#
# Constraints:
#
# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.