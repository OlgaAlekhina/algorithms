from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    strs_dict = defaultdict(list)
    for str in strs:
        sorted_str = ''.join(sorted(str))
        strs_dict[sorted_str].append(str)

    return list(strs_dict.values())


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Given an array of strings strs, group the
# anagrams
#  together. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.