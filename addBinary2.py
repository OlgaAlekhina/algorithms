def add_binary(a, b):
    l1 = len(a)
    l2 = len(b)
    if l1 >= l2:
        return binary_sum(a, b)
    else:
        return binary_sum(b, a)


def binary_sum(a, b, r=0):
    if b:
        bin_sum = int(a[-1]) + int(b[-1]) + r
    else:
        bin_sum = int(a[-1]) + r
    l1 = len(a)
    l2 = len(b)
    if l1 == 1:
        if bin_sum < 2:
            return str(bin_sum)
        elif bin_sum == 2:
            return '10'
        else:
            return '11'
    if bin_sum < 2:
        return binary_sum(a[:l1-1], b[:l2-1], r=0) + str(bin_sum)
    elif bin_sum == 2:
        return binary_sum(a[:l1-1], b[:l2-1], r=1) + '0'
    else:
        return binary_sum(a[:l1-1], b[:l2-1], r=1) + '1'


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