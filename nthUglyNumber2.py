def ugly_number(n: int) -> int:
    ugly_list = [0, 1] + [0] * (n - 1)
    p2, p3, p5, count = 1, 1, 1, 1
    while count < n:
        next_ugly = min(2 * ugly_list[p2], 3 * ugly_list[p3], 5 * ugly_list[p5])
        if next_ugly != ugly_list[count]:
            count += 1
            ugly_list[count] = next_ugly
        if next_ugly == 2 * ugly_list[p2]:
            p2 += 1
        elif next_ugly == 3 * ugly_list[p3]:
            p3 += 1
        else:
            p5 += 1

    return ugly_list[count]


print(ugly_number(800))

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return the nth ugly number.
#
#
#
# Example 1:
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:
#
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
#
#
# Constraints:
#
# 1 <= n <= 1690