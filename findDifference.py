from collections import Counter


def find_difference(s: str, t: str) -> str:
    char_dict = Counter(s + t)
    for key, val in char_dict.items():
        if val % 2 != 0:
            return key


print(find_difference("", "a"))

# You are given two strings s and t.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Return the letter that was added to t.
#
#
#
# Example 1:
#
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:
#
# Input: s = "", t = "y"
# Output: "y"
#
#
# Constraints:
#
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s and t consist of lowercase English letters.