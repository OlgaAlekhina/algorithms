def title_to_number(column_title: str) -> int:
    l = len(column_title)
    result = 0
    for i, j in zip(range(l), range(l - 1, -1, -1)):
        letter = ord(column_title[j]) - 64
        result += letter * 26 ** i

    return result


print(title_to_number("A"))


# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
# Example 1:
#
# Input: columnTitle = "A"
# Output: 1
# Example 2:
#
# Input: columnTitle = "AB"
# Output: 28
# Example 3:
#
# Input: columnTitle = "ZY"
# Output: 701
#
#
# Constraints:
#
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"]