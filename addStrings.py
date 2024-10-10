def add_strings(num1: str, num2: str) -> str:
    res, mem, max_len = '', 0, max(len(num1), len(num2))
    num1, num2 = num1.zfill(max_len), num2.zfill(max_len)
    for i in range(max_len - 1, -1, -1):
        str_sum = int(num1[i]) + int(num2[i]) + mem
        res += str(str_sum % 10)
        mem = 1 if str_sum > 9 else 0
    if mem:
        res += '1'

    return res[::-1]


print(add_strings("0", "0"))

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
#
#
#
# Example 1:
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.