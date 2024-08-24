from typing import List


def duplicate_zeroes(arr: List[int]) -> None:
    arr_len = len(arr)
    count = arr.count(0)
    for i in range(arr_len - 1, -1, -1):
        if arr[i] == 0:
            count -= 1
            if i + count < arr_len:
                arr[i + count] = 0
            if i + count + 1 < arr_len:
                arr[i + count + 1] = 0
        else:
            if i + count < arr_len:
                arr[i + count] = arr[i]

    print(arr)


print(duplicate_zeroes([1,0,2,3,0,4,5,0]))

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
#
#
#
# Example 1:
#
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
#
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
#
# Constraints:
#
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9