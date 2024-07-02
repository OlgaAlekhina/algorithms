from typing import List


def three_consecutive_odds(arr: List[int]) -> bool:
    count = 0
    for num in arr:
        if num % 2 == 0:
            count = 0
        else:
            count += 1
        if count == 3:
            return True

    return False


print(three_consecutive_odds([2,4,6]))

# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
#
#
# Example 1:
#
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:
#
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
#
#
# Constraints:
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000