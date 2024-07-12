"""
Учитывая две строки s и t длин m и n соответственно, верните минимальное окно
подстрока (sвключая дубликатыt) включается в окно таким образом, чтобы каждый
символ в из .
Если такой подстроки нет, верните пустую строку "".

Тестовые примеры будут сгенерированы таким образом, чтобы ответ был уникальным.

Пример 1:

Ввод: s = "ADOBECODEBANC", t = "ABC"
Вывод: "BANC"
Пояснение:
Минимальная подстрока окна "BANC" включает 'A', 'B' и 'C' из строки t.

Пример 2:

Ввод: s = "a", t = "a"
Вывод: "a"
Пояснение: Вся строка s является минимальным окном.
Пример 3:

Ввод: s = "a", t = "aa"
Вывод: ""
Объяснение: Оба 'a' из t должны быть включены в окно.
Поскольку в самом большом окне из s есть только одно 'a',
верните пустую строку.

Ограничения:

m == s.length
n == t.length
1 <= m, n <= 105
s и t состоят из прописных и строчных английских букв.

Продолжение: Не могли бы вы найти алгоритм,
который выполняется за O(m + n) время?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        # создаем словарь для символов из t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        # инициализируем переменные
        left, right = 0, 0
        required = len(dict_t)
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        # двигаем правый указатель
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            # двигаем левый указатель
            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


if __name__ == "__main__":
    sol = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))  # -> BANC

    s = "a"
    t = "a"
    print(sol.minWindow(s, t))  # -> a

    s = "bsdasdb"
    t = "ab"
    print(sol.minWindow(s, t))  # -> ""
