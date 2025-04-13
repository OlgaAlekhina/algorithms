from typing import List


def max_product(words: List[str]) -> int:
    words_sets, res = [], 0
    for word in words:
        words_sets.append((set(word), len(word)))
    for i in range(len(words_sets)):
        for j in range(i + 1, len(words_sets)):
            if not words_sets[i][0] & words_sets[j][0]:
                res = max(res, words_sets[i][1] * words_sets[j][1])

    return res


print(max_product(["a","aa","aaa","aaaa"]))

# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
#
#
#
# Example 1:
#
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:
#
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:
#
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#
# Constraints:
#
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.