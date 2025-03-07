"""
Даны два отсортированных массива nums1и nums2размером mи nсоответственно, вернуть медиану двух отсортированных массивов.

Общая сложность времени выполнения должна быть O(log (m+n)).



Пример 1:

Ввод: nums1 = [1,3], nums2 = [2]
 Вывод: 2,00000
 Объяснение: объединенный массив = [1,2,3], а медиана равна 2.
Пример 2:

Ввод: nums1 = [1,2], nums2 = [3,4]
 Вывод: 2,50000
 Пояснение: объединенный массив = [1,2,3,4], а медиана равна (2 + 3) / 2 = 2,5.


Ограничения:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List
import random


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Общая сложность времени выполнения O(log (m+n))"""

        n1 = len(nums1)
        n2 = len(nums2)

        # Для простоты предположим, что nums1 — меньший массив
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        left = (n1 + n2 + 1) // 2  # Вычислить размер левого раздела
        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2  # Вычислить средний индекс для nums1
            mid2 = left - mid1  # Вычислить средний индекс для nums2

            l1 = float("-inf")
            l2 = float("-inf")
            r1 = float("inf")
            r2 = float("inf")

            # Определите значения l1, l2, r1 и r2
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                # мы нашли медиану
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Двигаемся влево по массиву nums1
                # print("high = mid1 - 1")
                high = mid1 - 1
            else:
                # Двигаемся вправо по массиву nums1
                low = mid1 + 1
                # print("low = mid1 + 1")
        return (
            0  # Если код доходит до этого места, входные массивы не были отсортированы.
        )

    def foo(self, nums1: List[int], nums2: List[int]) -> float:
        """сложность времени выполнения  O(1/2(m+n))"""
        f = len(nums1) + len(nums2)
        i = 0
        j = 0
        mid = f // 2
        flag = f % 2
        t = 0
        res2 = 0
        while t <= mid:
            if i > len(nums1) - 1:
                res1 = nums2[j]
                j += 1
            elif j > len(nums2) - 1:
                res1 = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                res1 = nums2[j]
                j += 1
            else:
                res1 = nums1[i]
                i += 1
            t += 1
            if t > mid and flag:
                res = res1
            else:
                res = (res1 + res2) / 2
            print(res1)
            res2 = res1
        return res


def generate_sorted_random_list(start, end, count):
    # Генерируем случайные числа
    random_numbers = [random.randint(start, end) for _ in range(count)]
    # Сортируем список
    sorted_numbers = sorted(random_numbers)
    return sorted_numbers


if __name__ == "__main__":
    sol = Solution()

    nums1 = generate_sorted_random_list(-(10**6), 10**6, 1000)
    nums2 = generate_sorted_random_list(-(10**6), 10**6, 1000)
    # Объяснение: объединенный массив = [1,2,3], а медиана равна 2.
    print("->>", sol.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 9]
    nums2 = [2, 3, 4]  # Вывод: 2,50000
    # Пояснение: объединенный массив = [1,2,3,4], а медиана равна (2 + 3) / 2 = 2,5.
    print("->>", sol.findMedianSortedArrays(nums1, nums2))
