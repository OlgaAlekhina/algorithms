def is_ugly(n: int):
    if n < 1:
        return False
    primes = [x if x % 2 > 0 and x % 3 > 0 and x % 5 > 0 else 0 for x in range(n + 1)]
    for i in range(5, len(primes)):
        if primes[i] > 0 and n % primes[i] == 0:
            return False
        elif primes[i] > 0:
            primes[i] = 0
            for j in range(i * i, len(primes), i):
                primes[i] = 0

    return True


print(is_ugly(47))

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return true if n is an ugly number.
#
#
#
# Example 1:
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
#
# Constraints:
#
# -231 <= n <= 231 - 1