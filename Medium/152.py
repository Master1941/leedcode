"""
Учитывая массив целых чисел nums, найдите
подмассив
 в котором содержится самый большой товар, и верните товар.

Тестовые примеры генерируются таким образом, чтобы ответ помещался в 32-разрядное целое число.



Пример 1:

Входные данные: nums = [2,3,-2,4]
Результат:6
Пояснение: [2,3] содержит самый большой продукт 6.
Пример 2:

Входные данные: nums = [-2,0, -1]
Результат:0
Объяснение: Результат не может быть равен 2, потому что [-2,-1] не является подмассивом.


Ограничения:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
Произведение любого подмассива из nums гарантированно укладывается в 32-разрядное целое число.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """ """
        n = len(nums)
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, n):
            temp = max_so_far
            max_so_far = max(max_so_far * nums[i], min_so_far * nums[i], nums[i])
            min_so_far = min(temp * nums[i], min_so_far * nums[i], nums[i])
            result = max(result, max_so_far)

        return result


if __name__ == "__main__":
    sol = Solution()

    nums = [2, 3, -2, 4]  # Результат:6
    # Пояснение: [2,3] содержит самый большой продукт 6.
    print(sol.maxProduct(nums))

    nums = [-2, 0, -1]  # Результат:0
    # Объяснение: Результат не может быть равен 2, потому что [-2,-1] не является подмассивом.
    print(sol.maxProduct(nums))

    nums = [-2, 0, -1, 5, 6, 5, 9, 6, 0, 5, 65]
    print(sol.maxProduct(nums))
