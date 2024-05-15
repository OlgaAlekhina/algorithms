def convert_to_title(column_number: int) -> str:
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    c = column_number // 26 if column_number % 26 != 0 else column_number // 26 - 1
    if c == 0:
        return letters[column_number - 1]

    return convert_to_title(c) + letters[column_number - c * 26 - 1]
        
        
print(convert_to_title(96000000))




# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
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
# Input: columnNumber = 1
# Output: "A"
# Example 2:
#
# Input: columnNumber = 28
# Output: "AB"
# Example 3:
#
# Input: columnNumber = 701
# Output: "ZY"
#
#
# Constraints:
#
# 1 <= columnNumber <= 231 - 1