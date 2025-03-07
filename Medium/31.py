"""
Перестановка элементов массива целых чисел — это расположение его элементов в последовательности или линейном порядке.

Например, для arr = [1,2,3] все возможные перестановки arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
Следующая перестановка массива целых чисел — это следующая лексикографически большая перестановка его элементов. Если говорить более формально, то если все перестановки массива отсортированы в одном контейнере в лексикографическом порядке, то следующей перестановкой этого массива будет перестановка, следующая за ней в отсортированном контейнере. Если такое расположение невозможно, массив должен быть переставлен в наименьший возможный порядок (то есть отсортирован по возрастанию).

Например, следующая перестановка arr = [1,2,3] является [1,3,2].
Аналогично, следующая перестановка arr = [2,3,1] является [3,1,2].
В то время как следующая перестановка arr = [3,2,1] — это [1,2,3], потому что [3,2,1] не имеет лексикографически более крупной перестановки.
Учитывая массив целых чисел nums, найдите следующую перестановку nums.

Замена должна быть на месте и использовать только постоянную дополнительную память.



Пример 1:

Ввод: nums = [1,2,3]
Вывод: [1,3,2]
Пример 2:

Ввод: nums = [3,2,1]
Вывод: [1,2,3]
Пример 3:

Ввод: nums = [1,1,5]
Вывод: [1,5,1]


Ограничения:

1 <= nums.length <= 100
0 <= nums[i] <= 100"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                idx = i
                break
        else:
            nums.reverse()
            print(nums)
            return

        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        nums[idx + 1 :] = reversed(nums[idx + 1 :])
        print(nums)


if __name__ == "__main__":
    import random

    sol = Solution()
    nums = [random.randint(1, 2) for _ in range(100000)]
    nums = [i for i in range(100000, 0, -1)]
    # nums = [1, 1, 1, 1, 1]
    print(nums)
    sol.nextPermutation(nums)
