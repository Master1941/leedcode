"""
Вам выдается большое целое число, представленное в виде массива целых чисел,
digits где каждое digits[i] является ith цифрой целого числа.
Цифры упорядочены от наиболее значимых к наименее значимым слева направо.
Большое целое число не содержит никаких ведущих 0's.

Увеличьте большое целое число на единицу и верните результирующий массив цифр.

Пример 1:

Ввод: цифры = [1,2,3]
Вывод: [1,2,4]
Объяснение: Массив представляет целое число 123.
Увеличение на единицу дает 123 + 1 = 124.
Таким образом, результат должен быть [1,2,4].
Пример 2:

Ввод: цифры = [4,3,2,1]
Вывод: [4,3,2,2]
Объяснение: Массив представляет целое число 4321.
Увеличение на единицу дает 4321 + 1 = 4322.
Таким образом, результатом должно быть [4,3,2,2].
Пример 3:

Ввод: цифры = [9]
Вывод: [1,0]
Объяснение: Массив представляет целое число 9.
Увеличение на единицу дает 9 + 1 = 10.
Таким образом, результат должен быть [1,0].
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        flag = 1
        result = []
        for i in reversed(digits):
            if flag:
                if (i + 1) == 10:
                    result.append(0)
                else:
                    result.append(i + 1)
                    flag = 0
            else:
                result.append(i)
        if flag:
            result.append(1)
        print(result)
        result = list(reversed(result))
        return result

    def plusOne2(self, digits: List[int]) -> List[int]:
        """Лучшее решение."""
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        return [1]+digits


if __name__ == "__main__":
    sol = Solution()

    digits = [1, 2, 3]  # -> Output: [1,2,4]
    print(sol.plusOne(digits))

    digits = [4, 3, 2, 1]  # -> Output: [4,3,2,2]
    print(sol.plusOne(digits))

    digits = [9, 9]  # -> Output: [1,0,0]
    print(sol.plusOne2(digits))
