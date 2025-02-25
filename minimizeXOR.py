def minimize_XOR(num1: int, num2: int) -> int:
    set_bits1, set_bits2, a, b = 0, 0, num1, num2
    while a:
        if a & 1 == 1:
            set_bits1 += 1
        a >>= 1
    while b:
        if b & 1 == 1:
            set_bits2 += 1
        b >>= 1
    if set_bits1 == set_bits2:
        return num1
    num1_list = list(bin(num1).split('b')[1])
    if set_bits2 >= len(num1_list):
        return int('1' * set_bits2, 2)
    for i in range(len(num1_list)):
        if num1_list[i] == '1' and set_bits2 > 0:
            set_bits2 -= 1
        else:
            num1_list[i] = '0'
    if set_bits2:
        for i in range(len(num1_list) - 1, -1, -1):
            if num1_list[i] == '0':
                num1_list[i] = '1'
                set_bits2 -= 1
            if set_bits2 == 0:
                break
    return int(''.join(num1_list), 2)

        

print(minimize_XOR(1, 12))

# Given two positive integers num1 and num2, find the positive integer x such that:
#
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
#
# Return the integer x. The test cases are generated such that x is uniquely determined.
#
# The number of set bits of an integer is the number of 1's in its binary representation.
#
#
#
# Example 1:
#
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
# Example 2:
#
# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
#
#
# Constraints:
#
# 1 <= num1, num2 <= 109