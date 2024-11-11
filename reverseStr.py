def reverse_string(s: str, k: int) -> str:
    count, res, i = 0, '', 0
    while i < len(s):
        if count % 2 == 0:
            if (i + k) < len(s):
                res += s[i+k-1::-1] if i == 0 else s[i+k-1:i-1:-1]
            else:
                res += s[::-1] if i == 0 else s[:i-1:-1]
        else:
            res += s[i:i + k] if (i + k) < len(s) else s[i:]
        count += 1
        i += k

    return res


print(reverse_string("a", 2))

# https://leetcode.com/problems/reverse-string-ii/description/
#
#
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
#
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
#
#
#
# Example 1:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
#
# Input: s = "abcd", k = 2
# Output: "bacd"
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104