def judge_square_sum(c: int) -> bool:
    a = 0
    while a ** 2 <= c / 2:
        b = (c - a ** 2) ** 0.5
        if b.is_integer():
            return True
        a += 1

    return False


print(judge_square_sum(16596026))

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
#
#
#
# Example 1:
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
#
# Input: c = 3
# Output: false
#
#
# Constraints:
#
# 0 <= c <= 231 - 1