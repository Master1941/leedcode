"""
Если задана строка, s содержащая только символы '(', ')', '{' '}', '[' ']',, то определите, является ли введенная строка допустимой.

Входная строка допустима, если:

Открытые квадратные скобки должны быть закрыты скобками того же типа.
Открытые квадратные скобки должны быть закрыты в правильном порядке.
Каждой закрывающей скобке соответствует открывающая скобка того же типа.
 

Пример 1:

Ввод: s = "()"
Вывод: true
Пример 2:

Ввод: s = "()[]{}"
Вывод: true
Пример 3:

Ввод: s = "(]"
Вывод: false
 

Ограничения:

1 <= s.length <= 104
s состоит только из круглых скобок '()[]{}'.

"""

class Solution:
    '''https://leetcode.com/problems/valid-parentheses/'''
    def isValid(self, s: str) -> bool:
        a = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for char in s:
            if char in a:
                if not stack or stack.pop() != a[char]:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    sol = Solution()

    s = "["  # -> False
    print(sol.isValid(s))

    s = "([{()[]{}}])"  # -> True
    print(sol.isValid(s))

    s = "(]"  # -> False
    print(sol.isValid(s))
