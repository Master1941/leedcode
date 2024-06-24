"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Ограничения:

-2**31 <= x <= 2**31 - 1
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time} секунд")
        return result
    return wrapper


class Solution(object):
    """
    https://leetcode.com/problems/palindrome-number/description/?source=submission-ac
    """
    def isPalindrome(self, x: int) -> bool:
        """Перевести число в строку и сравнить побуквенно."""
        string = str(x)
        i = len(string) - 1
        j = 0
        while j < i:  
            if string[i] != string[j]:
                return False
            j += 1
            i -= 1
        return True
    
    def foo(self, x: int) -> bool:
        """Сравнить строки."""
        x_str=str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False
        
    def foo2(self, x: int) -> bool:
        """Перевернуть половину числа и сравнить."""
        r = 0
        o = x
        while ( o > r ):
            r = r * 10 + o % 10
            o = int(o / 10)
        return (o == r) or (o == int(r/10))


if __name__ == "__main__":
    sol = Solution()
    x = 12345654321
    print(sol.isPalindrome(x))
    print(sol.foo(x))
    print(sol.foo2(x))

