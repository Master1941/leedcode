"""
Учитывая целое число, columnNumberверните соответствующий заголовок столбца в том виде, в каком он отображается в таблице Excel.

Для примера:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Пример 1:

Ввод: номер столбца = 1
Вывод: "A"
Пример 2:

Ввод: номер столбца = 28
Вывод: "AB"
Пример 3:

Ввод: номер столбца = 701
Вывод: "ZY"


Ограничения:

1 <= columnNumber <= 231 - 1
"""

import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dictionary = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            0: "Z",
        }
        res = ""
        while columnNumber > 0:
            res = dictionary[columnNumber % 26] + res
            columnNumber = (columnNumber - 1) // 26
        return res

    def convertToTitle2(self, columnNumber: int) -> str:
        """Использует встроеный в Python список символов."""
        al = list(string.ascii_uppercase)
        temp = []

        while columnNumber > 0:
            columnNumber = columnNumber - 1
            temp.append(al[(columnNumber % 26)])
            columnNumber = columnNumber // 26
        temp.reverse()
        return "".join(temp)


if __name__ == "__main__":
    sol = Solution()

    col = 26 + 26 * 26 + 26**2 * 26 + (26**3) * 26 + (26**4) * 26  # Вывод: "ZZZZZ"
    print(sol.convertToTitle2(col))

    col = 1  #    Вывод: "A"
    print(sol.convertToTitle2(col))

    col = 28  #    Вывод: "AB"
    print(sol.convertToTitle2(col))

    col = 701  #    Вывод: "ZY"
    print(sol.convertToTitle2(col))

    title = chr(ord("A") + (col - 1) % 26)
    print(title, ord("A"), +(col - 1) % 26)

    print(list(string.ascii_uppercase))
