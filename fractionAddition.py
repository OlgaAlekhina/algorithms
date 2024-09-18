def fraction_addition(expression: str) -> str:
    exp_split = expression.split('/')
    nums, dens = [int(exp_split[0])], []
    for i in range(1, len(exp_split) - 1):
        ind = exp_split[i].find('+') if '+' in exp_split[i] else exp_split[i].find('-')
        dens.append(int(exp_split[i][:ind]))
        nums.append(int(exp_split[i][ind:]))
    dens.append(int(exp_split[-1]))
    max_den = dens[0]
    for i in range(1, len(dens)):
        a, b = max(max_den, dens[i]), min(max_den, dens[i])
        if a % b == 0:
            max_den = a
        else:
            while b:
                a, b = b, a % b
            max_den *= dens[i] // a
    max_num = sum([max_den // a * b for a, b in zip(dens, nums)])
    a, b = abs(max_den), abs(max_num)
    while b:
        a, b = b, a % b

    return str(max_num // a) + '/' + str(max_den // a)


print(fraction_addition("1/3-1/2"))

# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
#
# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
#
#
#
# Example 1:
#
# Input: expression = "-1/2+1/2"
# Output: "0/1"
# Example 2:
#
# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
#
# Input: expression = "1/3-1/2"
# Output: "-1/6"
#
#
# Constraints:
#
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.