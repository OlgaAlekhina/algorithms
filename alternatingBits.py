def has_alternating_bits(n: int) -> bool:
    cur = None
    while n:
        if n & 1 == cur:
            return False
        cur = n & 1
        n >>= 1

    return True


print(has_alternating_bits(2))

# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
#
# Constraints:
#
# 1 <= n <= 231 - 1