def word_pattern(pattern: str, s: str) -> bool:
    s_list = s.split(' ')
    if len(pattern) != len(s_list):
        return False
    words_set = set()
    words_dict = {}
    for i in range(len(pattern)):
        if pattern[i] not in words_dict:
            if s_list[i] in words_set:
                return False
            words_dict[pattern[i]] = s_list[i]
            words_set.add(s_list[i])
        else:
            if words_dict.get(pattern[i]) != s_list[i]:
                return False

    return True


print(word_pattern("a", "dog"))

# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
#
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
# Constraints:
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.