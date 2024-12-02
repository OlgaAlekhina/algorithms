from typing import List


def check_double(arr: List[int]) -> bool:
    nums_set = set()
    for num in arr:
        if num * 2 in nums_set:
            return True
        if num % 2 == 0 and num // 2 in nums_set:
            return True
        if num not in nums_set:
            nums_set.add(num)

    return False


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