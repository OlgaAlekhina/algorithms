from collections import defaultdict


def reverse_substring(s: str) -> bool:
    s_dict = defaultdict(set)
    for i in range(len(s) - 1):
        s_dict[s[i]].add(s[i + 1])
    for item in s_dict.items():
        for char in item[1]:
            if s_dict.get(char) and item[0] in s_dict.get(char):
                return True

    return False


print(reverse_substring("abcd"))

# Given a string s, find any
# substring
#  of length 2 which is also present in the reverse of s.
#
# Return true if such a substring exists, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "leetcode"
#
# Output: true
#
# Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".
#
# Example 2:
#
# Input: s = "abcba"
#
# Output: true
#
# Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".
#
# Example 3:
#
# Input: s = "abcd"
#
# Output: false
#
# Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.
#
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists only of lowercase English letters.