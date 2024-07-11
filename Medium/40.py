"""
Учитывая набор чисел-кандидатов (candidates) и целевое число (target),
найдите все уникальные комбинации в candidates, где числа-кандидаты в сумме
равны target.

Каждое число в candidates может быть использовано в комбинации только один раз.

Примечание: Набор решений не должен содержать повторяющихся комбинаций.

Пример 1:

Входные данные: кандидаты = [10,1,2,7,6,1,5], цель = 8
Выходные данные:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Пример 2:

Входные данные: кандидаты = [2,5,2,1,2], цель = 5
Выходные данные:
[
[1,2,2],
[5]
]

Ограничения:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0 and path not in res:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    # print(f"{i, start, candidates[i], candidates[i-1]}")
                    continue
                backtrack(i+1, target-candidates[i], path+[candidates[i]])
        candidates.sort()
        res = []
        backtrack(0, target, [])
        return res


if __name__ == "__main__":
    sol = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8  # --> [[1,1,6], [1,2,5], [1,7], [2,6]]
    print(sol.combinationSum2(candidates, target))

    candidates = [2, 5, 2, 1, 2]
    target = 5  # --> [[1,2,2], [5]]
    print(sol.combinationSum2(candidates, target))
