def convert_hex(num: int) -> str:
    if num == 0:
        return '0'
    conv_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    res = ''
    while num and len(res) < 8:
        res += str(num % 16) if num % 16 < 10 else conv_dict.get(num % 16)
        num //= 16
        
    return res[::-1]


print(convert_hex(26))

# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
#
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
#
# Note: You are not allowed to use any built-in library method to directly solve this problem.
#
#
#
# Example 1:
#
# Input: num = 26
# Output: "1a"
# Example 2:
#
# Input: num = -1
# Output: "ffffffff"
#
#
# Constraints:
#
# -231 <= num <= 231 - 1