# solution with O(n + m) complexity


from typing import List


def count_negatives(grid: List[List[int]]) -> int:
    res, row, column, columns = 0, len(grid) - 1, 0, len(grid[0])
    while row > -1:
        while column < columns:
            if grid[row][column] < 0:
                res += columns - column
                break
            column += 1
        row -= 1

    return res


print(count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
#
#
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
#
#
# Follow up: Could you find an O(n + m) solution?