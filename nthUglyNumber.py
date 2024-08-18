# brute force solution which got time exceed limits error on LeetCode

def ugly_number(n: int) -> int:
    def is_ugly(num):
        while num % 5 == 0:
            num //= 5
        while num % 3 == 0:
            num //= 3
        while num % 2 == 0:
            num //= 2
        return num == 1
    count, num = 0, 1
    while True:
        if is_ugly(num):
            count += 1
        if count == n:
            return num
        num += 1


print(ugly_number(19))

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