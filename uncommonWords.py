from typing import List


def uncommon_words(s1: str, s2: str) -> List[str]:
    s1_list = s1.split(' ')
    s2_list = s2.split(' ')
    res_dict = {}
    for s in s1_list:
        if s not in s2_list:
            if s in res_dict:
                res_dict[s] += 1
            else:
                res_dict[s] = 1
    for s in s2_list:
        if s not in s1_list:
            if s in res_dict:
                res_dict[s] += 1
            else:
                res_dict[s] = 1

    return [key for key in res_dict if res_dict.get(key) == 1]


print(uncommon_words("banana", "apple apple"))

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