from typing import List


def vowel_strings(words: List[str], queries: List[List[int]]) -> List[int]:
    res = []
    vowels_tuple = ('a', 'e', 'i', 'o', 'u')
    words[0] = 1 if words[0].startswith(vowels_tuple) and words[0].endswith(vowels_tuple) else 0
    for i in range(1, len(words)):
         words[i] = words[i - 1] + 1 if words[i].startswith(vowels_tuple) and words[i].endswith(vowels_tuple) else words[i - 1]
    for q in queries:
        ans = words[q[1]] - words[q[0] - 1] if q[0] > 0 else words[q[1]]
        res.append(ans)

    return res


print(vowel_strings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))

# You are given a 0-indexed array of strings words and a 2D array of integers queries.
#
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
#
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
#
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
#
#
#
# Example 1:
#
# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
# Example 2:
#
# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# Explanation: Every string satisfies the conditions, so we return [3,2,1].
#
#
# Constraints:
#
# 1 <= words.length <= 105
# 1 <= words[i].length <= 40
# words[i] consists only of lowercase English letters.
# sum(words[i].length) <= 3 * 105
# 1 <= queries.length <= 105
# 0 <= li <= ri < words.length