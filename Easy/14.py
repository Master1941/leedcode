"""
Напишите функцию для поиска самой длинной строки общего префикса среди массива строк.

Если общего префикса нет, верните пустую строку "".

Ограничения:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] состоит только из строчных английских букв.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Сортируем список строк и проверяем только первую и последнюю строку."""
        if not strs:
            return ""
        strs.sort()
        prefix=strs[0]
        last=strs[-1]
        i = 0
        while i < len(prefix) and i < len(last) and prefix[i] == last[i]:
            i += 1
        return prefix[:i]


if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]  # -> "fl"
    print(sol.longestCommonPrefix(strs))
    strs = []  # -> ""
    print(sol.longestCommonPrefix(strs))
    strs = [
        "dog",
        "racecar",
        "car",
        ]  # -> ""
    print(sol.longestCommonPrefix(strs))

