from typing import List


def find_words(words: List[str]) -> List[str]:
    set1, set2, set3, res = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"), []
    for word in words:
        if set(word.lower()).issubset(set1) or set(word.lower()).issubset(set2) or set(word.lower()).issubset(set3):
            res.append(word)

    return res


print(find_words(["Hello","Alaska","Dad","Peace"]))

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# 
# In the American keyboard:
# 
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# 
#  
# 
# Example 1:
# 
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:
# 
# Input: words = ["omk"]
# Output: []
# Example 3:
# 
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
#  
# 
# Constraints:
# 
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 