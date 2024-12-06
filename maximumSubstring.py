from collections import defaultdict


def maximum_substring(s: str) -> int:
    char_dict = defaultdict(int)
    char_dict[s[0]] = 1
    triple = ''
    start = end = max_len = 0
    while end < len(s) - 1:
        while end < len(s) - 1 and not triple:
            end += 1
            char_dict[s[end]] += 1
            if char_dict[s[end]] == 3:
                triple = s[end]
                max_len = max(max_len, end - start)
        while end < len(s) - 1 and triple:
            char_dict[s[start]] -= 1
            if s[start] == triple:
                triple = ''
                max_len = max(max_len, end - start)
            start += 1
    if not triple:
        max_len = max(max_len, end - start + 1)

    return max_len


print(maximum_substring("bcbbbcba"))


# Given a string s, return the maximum length of a
# substring
#  such that it contains at most two occurrences of each character.
#
#
# Example 1:
#
# Input: s = "bcbbbcba"
#
# Output: 4
#
# Explanation:
#
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:
#
# Input: s = "aaaa"
#
# Output: 2
#
# Explanation:
#
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
#
#
# Constraints:
#
# 2 <= s.length <= 100
# s consists only of lowercase English letters.