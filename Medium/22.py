"""
Учитывая n пары круглых скобок, напишите функцию для генерации всех комбинаций
правильно сформированных круглых скобок.

Пример 1:

Ввод: n = 3
Вывод:  ["((()))","(()())","(())()","()(())","()()()"]
Пример 2:

Ввод: n = 1
Вывод: ["()"]

Ограничения:

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result

    def backtrack(
        self, result, current_str, open_count, close_count, max_count
    ):
        if len(current_str) == max_count * 2:
            result.append(current_str)
            return

        if open_count < max_count:
            self.backtrack(
                result,
                current_str + "(",
                open_count + 1,
                close_count,
                max_count
            )

        if close_count < open_count:
            self.backtrack(
                result,
                current_str + ")",
                open_count,
                close_count + 1,
                max_count
            )


if __name__ == "__main__":
    sol = Solution()

    n = 6
    print(sol.generateParenthesis(n))

    # n = 5
    # print(sol.generateParenthesis(n))
