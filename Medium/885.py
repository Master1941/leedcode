"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east.
The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary,
we continue our walk outside the grid (but may return to the grid boundary later.).
Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:

Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""

from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        """ """
        count = 1
        res = [[rStart, cStart]]
        flag = "c"
        delta_row = delta_col = 1
        dr = dc = 1
        while rows * cols > count:
            if flag == "c":
                cStart = cStart + 1
                dc -= 1
                if not dc:
                    delta_col += 1
                    dc = delta_col
                    flag = "r"
            elif flag == "r":
                rStart = rStart + 1
                dr -= 1
                if not dr:
                    flag = "-c"
                    delta_row += 1
                    dr = delta_row
            elif flag == "-c":
                cStart = cStart - 1
                dc -= 1
                if not dc:
                    flag = "-r"
                    delta_col += 1
                    dc = delta_col
            elif flag == "-r":
                rStart = rStart - 1
                dr -= 1
                if not dr:
                    flag = "c"
                    delta_row += 1
                    dr = delta_row
            if 0 <= rStart < rows and 0 <= cStart < cols:
                count += 1
                res.append([rStart, cStart])
        return res


if __name__ == "__main__":
    sol = Solution()
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    res = sol.spiralMatrixIII(rows, cols, rStart, cStart)
    print(res)  # Output: [[0, 0], [0, 1], [0, 2], [0, 3]]

    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    res = sol.spiralMatrixIII(rows, cols, rStart, cStart)
    print(res)
    Output = [
        [1, 4],
        [1, 5],
        [2, 5],
        [2, 4],
        [2, 3],
        [1, 3],
        [0, 3],
        [0, 4],
        [0, 5],
        [3, 5],
        [3, 4],
        [3, 3],
        [3, 2],
        [2, 2],
        [1, 2],
        [0, 2],
        [4, 5],
        [4, 4],
        [4, 3],
        [4, 2],
        [4, 1],
        [3, 1],
        [2, 1],
        [1, 1],
        [0, 1],
        [4, 0],
        [3, 0],
        [2, 0],
        [1, 0],
        [0, 0],
    ]
