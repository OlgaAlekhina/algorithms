def count_segments(s: str) -> int:
    res, flag = 0, False
    s = s.strip()
    for char in s:
        if char == ' ' and flag:
            res += 1
            flag = False
        elif char != ' ':
            flag = True

    return res + 1 if flag else res


print(count_segments(""))

# Однострочное решение:   return len(s.split())

# Given a string s, return the number of segments in the string.
#
# A segment is defined to be a contiguous sequence of non-space characters.
#
#
#
# Example 1:
#
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:
#
# Input: s = "Hello"
# Output: 1
#
#
# Constraints:
#
# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.