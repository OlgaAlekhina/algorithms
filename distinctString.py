from typing import List
from collections import defaultdict


def distinct_string(arr: List[str], k: int) -> str:
    str_dict = defaultdict(int)
    for s in arr:
        str_dict[s] += 1
    count = 0
    for key in str_dict:
        if str_dict[key] == 1:
            count += 1
            if count == k:
                return key

    return ''


print(distinct_string(["a"], 1))

# A distinct string is a string that is present only once in an array.
#
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
#
# Note that the strings are considered in the order in which they appear in the array.
#
#
#
# Example 1:
#
# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned.
# Example 2:
#
# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# Example 3:
#
# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
#
#
# Constraints:
#
# 1 <= k <= arr.length <= 1000
# 1 <= arr[i].length <= 5
# arr[i] consists of lowercase English letters.