def get_row(row_index: int):
    if row_index == 0:
        return [1]
    i = 2
    res = [1, 1]
    while i <= row_index:
        cur_row = [1]
        for j in range(i - 1):
            cur_row.append(res[j] + res[j + 1])
        cur_row.append(1)
        res = cur_row
        i += 1

    return res
        
        
print(get_row(6))

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]
# Example 3:
#
# Input: rowIndex = 1
# Output: [1,1]
#
#
# Constraints:
#
# 0 <= rowIndex <= 33
#
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?