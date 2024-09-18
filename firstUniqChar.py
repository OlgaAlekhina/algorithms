from collections import Counter


def first_uniq_char(s: str) -> int:
    char_dict = Counter(s)
    for ind, char in enumerate(s):
        if char_dict.get(char) == 1:
            return ind

    return -1


print(first_uniq_char("a"))

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
#
#
# Example 1:
#
# Input: s = "leetcode"
#
# Output: 0
#
# Explanation:
#
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
#
# Input: s = "loveleetcode"
#
# Output: 2
#
# Example 3:
#
# Input: s = "aabb"
#
# Output: -1
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.