def harshad_number(x: int) -> int:
    num, dig_sum = x, 0
    while num:
        dig_sum += num % 10
        num //= 10

    return dig_sum if x % dig_sum == 0 else -1


# An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.
#
#
#
# Example 1:
#
# Input: x = 18
#
# Output: 9
#
# Explanation:
#
# The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.
#
# Example 2:
#
# Input: x = 23
#
# Output: -1
#
# Explanation:
#
# The sum of digits of x is 5. 23 is not divisible by 5. So 23 is not a Harshad number and the answer is -1.
#
#
#
# Constraints:
#
# 1 <= x <= 100