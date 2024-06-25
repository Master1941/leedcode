"""
Значение       символа
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
Например, 2 записывается как II римскими цифрами, просто складываются две единицы. 12 записывается как XII, что означает просто X + II. Число 27 записывается как XXVII, что является XX + V + II.

Римские цифры обычно записываются от наибольшего к наименьшему слева направо. Однако цифра для четырех таковой не является IIII. Вместо этого число четыре записывается как IV. Поскольку единица стоит перед пятеркой, мы вычитаем ее, получая четыре. Тот же принцип применим к числу девять, которое записывается как IX. Существует шесть случаев, когда используется вычитание:

I может быть помещен перед V (5) и X (10), чтобы получились 4 и 9.
X может быть помещен перед L (50) и C (100), чтобы составить 40 и 90.
C может быть помещен перед D (500) и M (1000), чтобы получить 400 и 900.
Если задана римская цифра, преобразуйте ее в целое число.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        i = 0
        while i < len(s)-1:
            if translations.get(s[i]) < translations.get(s[i+1]):
                result -= translations.get(s[i])
            else:
                result += translations.get(s[i])
            i += 1
        return(result + translations[s[-1]])



    def romanToInt_2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
    
if __name__ == "__main__":
    sol = Solution()

    # s = "III" 
    # s = "LVIII"
    s = "MCMXCIV" 

    print(sol.romanToInt(s))
    print(sol.romanToInt_2(s))
