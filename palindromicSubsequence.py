from collections import defaultdict


def palindromic_subsequences(s: str) -> int:
    res = 0
    letters_dict = defaultdict(list)
    for i, char in enumerate(s):
        letters_dict[char].append(i)
    for key in letters_dict.keys():
        char = letters_dict.get(key)
        min_ind, max_ind = char[0], char[-1]
        if max_ind - min_ind > 1:
            for val in letters_dict.values():
                for ind in val:
                    if min_ind < ind < max_ind:
                        res += 1
                        break
                    elif ind >= max_ind:
                        break

    return res


print(palindromic_subsequences("bbcbaba"))

# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 105
# s consists of only lowercase English letters.