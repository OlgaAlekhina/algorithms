from typing import List
from collections import Counter


def uncommon_words(s1: str, s2: str) -> List[str]:
    s1_dict, s2_dict, res = Counter(s1.split()), Counter(s2.split()), []
    for key, val in s1_dict.items():
        if val == 1 and key not in s2_dict:
            res.append(key)
    for key, val in s2_dict.items():
        if val == 1 and key not in s1_dict:
            res.append(key)

    return res


print(uncommon_words("this apple is sweet", "this apple is sour"))

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
#
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.