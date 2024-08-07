def add_digits(num: int) -> int:
    while num > 9:
        new_num = 0
        while num:
            new_num += num % 10
            num //= 10
        num = new_num

    return num


print(add_digits(29))

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#
#
#
# Example 1:
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# Example 2:
#
# Input: num = 0
# Output: 0
#
#
# Constraints:
#
# 0 <= num <= 231 - 1
#
#
# Follow up: Could you do it without any loop/recursion in O(1) runtime?