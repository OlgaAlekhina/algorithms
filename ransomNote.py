from collections import Counter


def ransom_note(ransom_note: str, magazine: str) -> bool:
    letters_dict = Counter(magazine)
    for char in ransom_note:
        if letters_dict.get(char, 0) < 1:
            return False
        letters_dict[char] -= 1

    return True


print(ransom_note("a", "b"))

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
#
#
#
# https://leetcode.com/problems/ransom-note/description/