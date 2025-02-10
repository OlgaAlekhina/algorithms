def special_chars(word: str) -> int:
    char_list = [0] * 26
    for char in word:
        if char.islower():
            ind = ord(char) - ord('a')
            if char_list[ind] == 2:
                char_list[ind] = 3
            elif char_list[ind] == 0:
                char_list[ind] = 1
        else:
            ind = ord(char) - ord('A')
            if char_list[ind] == 1:
                char_list[ind] = 3
            elif char_list[ind] == 0:
                char_list[ind] = 2

    return char_list.count(3)


print(special_chars("abBCab"))

# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
#
# Return the number of special letters in word.
#
#
#
# Example 1:
#
# Input: word = "aaAbcBC"
#
# Output: 3
#
# Explanation:
#
# The special characters in word are 'a', 'b', and 'c'.
#
# Example 2:
#
# Input: word = "abc"
#
# Output: 0
#
# Explanation:
#
# No character in word appears in uppercase.
#
# Example 3:
#
# Input: word = "abBCab"
#
# Output: 1
#
# Explanation:
#
# The only special character in word is 'b'.
#
#
#
# Constraints:
#
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.