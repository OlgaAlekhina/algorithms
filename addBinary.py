def add_binary(a, b):
    l1 = len(a)
    l2 = len(b)
    dec_number1 = 0
    dec_number2 = 0
    for i, j in zip(range(l1-1, -1, -1), range(l1)):
        dec_number1 += int(a[i]) * 2 ** j
    for i, j in zip(range(l2 - 1, -1, -1), range(l2)):
        dec_number2 += int(b[i]) * 2 ** j
    dec_sum = dec_number1 + dec_number2
    bin_list = []
    if dec_sum == 0:
        return '0'
    while dec_sum > 0:
        bin_list.append(str(dec_sum % 2))
        dec_sum = dec_sum // 2
    return ''.join(bin_list)[::-1]


print(add_binary('10', '1010'))
            


# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.