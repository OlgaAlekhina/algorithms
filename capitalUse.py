def detect_capital_use(word: str) -> bool:
    l = len(word)
    if l == 1:
        return True
    if word[0].islower():
        for char in word:
            if char.isupper():
                return False
    elif word[0].isupper() and word[1].islower():
        for i in range(1, l):
            if word[i].isupper():
                return False
    else:
        for i in range(1, l):
            if word[i].islower():
                return False

    return True


print(detect_capital_use("Kl"))

# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
#
#
#
# Example 1:
#
# Input: word = "USA"
# Output: true
# Example 2:
#
# Input: word = "FlaG"
# Output: false
#
#
# Constraints:
#
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.