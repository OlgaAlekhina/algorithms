from typing import List


def spiral_matrix(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    res = [[rStart, cStart]]
    res_len = rows * cols
    cur_row, cur_col, count = rStart, cStart, 2
    while res_len > 1:
        for cur_col in range(cur_col + 1, cur_col + count):
            if 0 <= cur_col < cols and 0 <= cur_row < rows:
                res.append([cur_row, cur_col])
                res_len -= 1
        for cur_row in range(cur_row + 1, cur_row + count):
            if 0 <= cur_col < cols and 0 <= cur_row < rows:
                res.append([cur_row, cur_col])
                res_len -= 1
        count += 1
        for cur_col in range(cur_col - 1, cur_col - count, -1):
            if 0 <= cur_col < cols and 0 <= cur_row < rows:
                res.append([cur_row, cur_col])
                res_len -= 1
        for cur_row in range(cur_row - 1, cur_row - count, -1):
            if 0 <= cur_col < cols and 0 <= cur_row < rows:
                res.append([cur_row, cur_col])
                res_len -= 1
        count += 1

    return res


print(spiral_matrix(5, 6, 4, 5))

# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the order you visited them.
#
#
#
# Example 1:
#
#
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# Example 2:
#
#
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
#
# Constraints:
#
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols