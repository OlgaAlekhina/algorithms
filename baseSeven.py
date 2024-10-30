def base_seven(num: int) -> str:
    if num == 0:
        return '0'
    res = '' if num >= 0 else '-'
    num = abs(num)
    while num:
        res += str(num % 7)
        num //= 7

    return res[::-1] if res.isdigit() else '-' + res[:0:-1]


print(base_seven(-70))

# Given an integer num, return a string of its base 7 representation.
#
#
#
# Example 1:
#
# Input: num = 100
# Output: "202"
# Example 2:
#
# Input: num = -7
# Output: "-10"
#
#
# Constraints:
#
# -107 <= num <= 107