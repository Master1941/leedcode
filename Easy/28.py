"""

Учитывая две строки needle и haystack, верните индекс первого вхождения
из needle в haystack, или -1 если needle не является частью haystack.


Пример 1:

Входные данные: haystack = "sadbutsad", needle = "sad"
Выходные данные: 0
Объяснение: "sad" встречается с индексами 0 и 6.
Первое вхождение имеет индекс 0, поэтому мы возвращаем 0.
Пример 2:

Входные данные: haystack = "leetcode", needle = "leeto"
Выходные данные: -1
Объяснение: "leeto" не встречается в "leetcode", поэтому мы возвращаем -1.
 

Ограничения:

1 <= haystack.length, needle.length <= 104
haystack и needle состоят только из строчных английских символов.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        result = j = 0 
        while result <= len(haystack) - len(needle):
            print(result, j)
            if j == len(needle):
                return result 
            if haystack[result + j] ==  needle[j]:
                print(haystack[result + j])
                j += 1
                continue
            result += 1
            j = 0


if __name__ == "__main__":
    sol = Solution()
    haystack = "sardbutsad"
    needle = "sad"  # -> 0
    print(sol.strStr(haystack, needle))

    haystack = "leetcode"
    needle = "leeto"  # -> -1  
    print(sol.strStr(haystack, needle))

