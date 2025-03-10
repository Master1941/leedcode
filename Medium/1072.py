"""
1072. Переверните столбцы, чтобы получить максимальное количество одинаковых строк
Средний
Темы
Компании
Подсказка
Вам дана m x n двоичная матрица matrix.

Вы можете выбрать любое количество столбцов в матрице и перевернуть каждую ячейку в этом столбце (т. е. изменить значение ячейки с 0 на 1 или наоборот).

Верните максимальное количество строк, в которых все значения равны после некоторого количества перестановок.



Пример 1:

Ввод: матрица = [[0,1],[1,1]]
Вывод: 1
Объяснение: После перестановки значений в 1 строке все значения равны.
Пример 2:

Входные данные: матрица = [[0,1],[1,0]]
Выходные данные: 2
Объяснение: после перестановки значений в первом столбце обе строки имеют одинаковые значения.
Пример 3:

Ввод: матрица = [[0,0,0],[0,0,1],[1,1,0]]
Вывод: 2
Пояснение: после перестановки значений в первых двух столбцах последние две строки имеют одинаковые значения.


Ограничения:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] является либо 0, либо 1.
"""

from typing import List, Counter
import operator


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """ """
        count = Counter(
            tuple(row if row[0] else map(operator.not_, row)) for row in matrix
        )

        return max(count.values())


if __name__ == "__main__":
    sol = Solution()
    # Example 1:

    matrix = [[0, 1], [1, 1]]
    print(sol.maxEqualRowsAfterFlips(matrix))
    Output: 1
    # Explanation: After flipping no values, 1 row has all values equal.
    # Example 2:

    matrix = [[0, 1], [1, 0]]
    print(sol.maxEqualRowsAfterFlips(matrix))
    Output: 2
    # Explanation: After flipping values in the first column, both rows have equal values.
    # Example 3:

    matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(sol.maxEqualRowsAfterFlips(matrix))
    Output: 2
    # Explanation: After flipping values in the first two columns, the last two rows have equal values.
