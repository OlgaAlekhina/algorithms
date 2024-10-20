def repeated_pattern(s: str) -> bool:
    len_s = len(s)
    for i in range(2, len_s + 1):
        if len_s % i == 0:
            pattern_len = len_s // i
            pattern = s[:pattern_len]
            for j in range(1, i):
                if s[j * pattern_len:(j+1)*pattern_len] != pattern:
                    break
            else:
                return True

    return False


print(repeated_pattern("a"))

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
#
#
#
# Example 1:
#
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:
#
# Input: s = "aba"
# Output: false
# Example 3:
#
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of lowercase English letters.