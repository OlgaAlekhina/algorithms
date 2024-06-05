from collections import Counter


def common_chars(words):
    com_dict = Counter(min(words, key=len))
    for word in words:
        word_dict = Counter(word)
        for key in com_dict:
            if key not in word_dict:
                com_dict[key] = 0
            else:
                if com_dict.get(key) > word_dict.get(key):
                    com_dict[key] = word_dict.get(key)
    com_chars = []
    for key, val in com_dict.items():
        com_chars += [key] * val

    return com_chars


print(common_chars(["coool","looock","coook"]))

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.