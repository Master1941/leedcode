"""
Учитывая отсортированный массив различных целых чисел и целевое значение,
верните индекс, если целевое значение найдено. Если нет, верните индекс туда,
где он был бы, если бы он был вставлен по порядку.

Вы должны написать алгоритм со O(log n) сложностью во время выполнения.


Пример 1:

Ввод: nums = [1,3,5,6], target = 5
Вывод: 2
Пример 2:

Ввод: nums = [1,3,5,6], target = 2
Вывод: 1
Пример 3:

Ввод: nums = [1,3,5,6], target = 7
Вывод: 4


Ограничения:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums содержит различные значения, отсортированные в порядке возрастания.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
           if nums[i] == target:
               return i
           if nums[i] > target:
               return i    
        return (i + 1)
    

if __name__ == "__main__":
    sol = Solution()

    nums = [1, 3, 5, 6]
    target = 5  # Вывод: 2
    print(sol.searchInsert(nums=nums, target=target))

    nums = [1, 3, 5, 6]
    target = 2  # Вывод: 1
    print(sol.searchInsert(nums=nums, target=target))

    nums = [1, 3, 5, 6]
    target = 7  # Вывод: 4
    print(sol.searchInsert(nums=nums, target=target))
