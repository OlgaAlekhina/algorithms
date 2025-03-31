def count_odds(low: int, high: int) -> int:
    int_numbers = high - low + 1
    if low % 2 == 0 or (low % 2 > 0 and int_numbers % 2 == 0):
        return int_numbers // 2
    return int_numbers // 2 + 1


print(count_odds(low = 0, high = 0))

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
#
#
#
# Example 1:
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
#
# Constraints:
#
# 0 <= low <= high <= 10^9