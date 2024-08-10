from collections import Counter
from typing import List


def count_characters(words: List[str], chars: str) -> int:
    len_chars = len(chars)
    chars_dict = Counter(chars)
    res = 0
    for word in words:
        valid = True
        len_word = len(word)
        if len_word > len_chars:
            continue
        word_dict = Counter(word)
        for key, val in word_dict.items():
            if key not in chars_dict or val > chars_dict.get(key):
                valid = False
                break
        if valid:
            res += len_word

    return res


print(count_characters(["hell"], "hello"))

# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.