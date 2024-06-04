from collections import Counter


def longest_palindrome(s: str) -> int:
    char_dict = Counter(s)
    len_pal, odd_char = 0, 0
    for val in char_dict.values():
        if val % 2 != 0:
            len_pal += val - 1
            if not odd_char:
                odd_char = 1
        else:
            len_pal += val

    return len_pal + odd_char if len_pal != 0 else 1


print(longest_palindrome("AAll"))

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#
#
#
# Example 1:
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.