from typing import List


def check_double(arr: List[int]) -> bool:
    def sort_arr(num):
        if num < 0:
            return 1/num
        return num
    arr.sort(key=sort_arr)
    double = arr[0] * 2
    for i in range(1, len(arr)):
        if (arr[i] < 0 and arr[i] <= double) or (arr[i] >= 0 and arr[i] >= double):
            double = i - 1
            break
    else:
        return False
    for i in range(len(arr)):
        if double == i:
            double += 1
        if double == len(arr) - 1 and arr[i] * 2 > arr[double]:
            return False
        while double < len(arr) and ((arr[double] >= 0 and arr[i] * 2 > arr[double]) or (arr[double] < 0 and arr[i] * 2 < arr[double])):
            double += 1
        if double > len(arr) - 1:
            return False
        if arr[i] * 2 == arr[double]:
            return True


print(check_double([-20,8,-6,-14,0,-19,14,4]))

# Given an array arr of integers, check if there exist two indices i and j such that :
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
#
#
# Example 1:
#
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:
#
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
#
#
# Constraints:
#
# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103