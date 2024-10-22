"""
Имеется целочисленный массив nums, отсортированный по возрастанию (с отдельными значениями).

Перед передачей в вашу функцию numsвозможно,
поворачивается по неизвестному индексу поворота k (1 <= k < nums.length) таким образом,
что результирующий массив является
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (с индексацией 0). Например, [0,1,2,4,5,6,7]
может быть повернут по индексу поворота 3 и стать [4,5,6,7,0,1,2].

Учитывая массив nums после возможного поворота и целое число target,
верните индекс target, если он находится в nums, или -1 если его нет в nums.

Вы должны написать алгоритм со O(log n) сложностью во время выполнения.



Пример 1:

Ввод: nums = [4,5,6,7,0,1,2], target = 0
Вывод: 4
Пример 2:

Ввод: nums = [4,5,6,7,0,1,2], target = 3
Вывод: -1
Пример 3:

Ввод: nums = [1], target = 0
Вывод: -1


Ограничения:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
Все значения nums являются уникальными.
nums представляет собой массив по возрастанию, который возможно поворачивать.
-104 <= target <= 104
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Алгоритм со O(log n) сложностью во время выполнения"""
        low = 0
        high = len(nums) - 1

        if not len(nums):
            return -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] == target:
                return low

            if nums[high] == target:
                return high

            if nums[mid] >= nums[low]:
                if target < nums[low] or target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[high] > target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    candidates = [4, 5, 6, 7, 0, 1, 2, 3]
    target = 0
    print(sol.search(candidates, target))

    candidates = [8, 9, 2, 3, 4]
    target = 9
    print(sol.search(candidates, target))

    candidates = [*range(6, 60)] + [*range(6)]
    target = 3
    print(sol.search(candidates, target))
