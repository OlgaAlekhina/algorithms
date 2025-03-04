def check_powers(n: int) -> bool:
    powers_list, i = [], 0
    while True:
        power = 3 ** i
        if power <= 10000000:
            powers_list.append(power)
            i += 1
        else:
            break
    for i in range(len(powers_list) - 1, -1, -1):
        if n - powers_list[i] == 0:
            return True
        elif n - powers_list[i] > 0:
            n -= powers_list[i]
            if n >= powers_list[i]:
                return False



print(check_powers(800))

# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
#
# An integer y is a power of three if there exists an integer x such that y == 3x.
#
#
#
# Example 1:
#
# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32
# Example 2:
#
# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34
# Example 3:
#
# Input: n = 21
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 107