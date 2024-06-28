"""
26. Удалить дубликаты из отсортированного массива
Легко
Темы - Массив, Два указателя

Учитывая, что массив целых чисел nums отсортирован в неубывающем порядке, удалите дубликаты на месте таким образом, чтобы каждый уникальный элемент появлялся только один раз. Относительный порядок элементов должен быть таким же. Затем верните количество уникальных элементов в nums.

Учтите количество уникальных элементов nums, которое должно быть k, чтобы быть принятым, вам нужно выполнить следующие действия:

Измените массив nums таким образом, чтобы первые k элементы nums содержали уникальные элементы в том порядке, в котором они присутствовали nums изначально. Остальные элементы nums не так важны, как размер nums.
Возвратk.
Пользовательская оценка:

Судья протестирует ваше решение с помощью следующего кода:

int[] nums = [...]; // Входной массив 
int[] expectedNums = [...]; // Ожидаемый ответ правильной длины

int k = удаленные дубликаты (числа); // Вызывает вашу реализацию

assert k == Ожидаемые числа.длина; 
for (int i = 0; i < k; i ++) {
 утвердить числа [i] == Ожидаемые числа [i]; 
}
Если все утверждения подтвердятся, то ваше решение будет принято.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]  # ->  2, nums = [1,2,_]
    k = sol.removeDuplicates(nums)
    print(k, nums)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # ->  5, nums = [0,1,2,3,4,_,_,_,_,_]
    k = sol.removeDuplicates(nums)
    print(k, nums)
