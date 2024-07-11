def reverse_parenthesis(s: str) -> str:
    s_list = list(s)
    res_list = []
    for char in s_list:
        sub_list = []
        if char == ')':
            while res_list[-1] != '(':
                sub_list.append(res_list.pop())
            res_list.pop()
            res_list.extend(sub_list)
        else:
            res_list.append(char)

    return ''.join(res_list)


print(reverse_parenthesis("fu(ed)(et(oc))el"))

# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.
#
#
#
# Example 1:
#
# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:
#
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
# Example 3:
#
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.