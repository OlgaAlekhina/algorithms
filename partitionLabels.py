from typing import List
from collections import Counter


def partition_labels(s: str) -> List[int]:
    char_freq, count, char_set, res = Counter(s), 1, set(), []
    for char in s:
        char_freq[char] -= 1
        if char_freq[char] > 0:
            count += 1
            char_set.add(char)
        else:
            if char in char_set:
                char_set.remove(char)
            if char_set:
                count += 1
            else:
                res.append(count)
                count = 1

    return res


print(partition_labels("e"))

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#
# Return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.