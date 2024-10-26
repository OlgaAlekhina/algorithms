from collections import Counter


def balloons_number(text: str) -> int:
    char_dict = Counter(text)

    return min(char_dict.get('a', 0), char_dict.get('b', 0), char_dict.get('n', 0), char_dict.get('l', 0) // 2, char_dict.get('o', 0) // 2)


print(balloons_number("balloonballoonballoonballoonballoonballoonballoonballoonn"))

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
#
#
# Example 1:
#
#
#
# Input: text = "nlaebolko"
# Output: 1
# Example 2:
#
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:
#
# Input: text = "leetcode"
# Output: 0
#
#
# Constraints:
#
# 1 <= text.length <= 104
# text consists of lower case English letters only.
#