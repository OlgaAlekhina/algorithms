def largest_group(n: int) -> int:
    groups = [0] * 37
    for num in range(1, n + 1):
        dig_sum = 0
        while num:
            dig_sum += num % 10
            num //= 10
        groups[dig_sum] += 1
    max_size = max(groups)

    return groups.count(max_size)


print(largest_group(2))

# You are given an integer n.
#
# Each number from 1 to n is grouped according to the sum of its digits.
#
# Return the number of groups that have the largest size.
#
#
#
# Example 1:
#
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# Example 2:
#
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
#
#
# Constraints:
#
# 1 <= n <= 104