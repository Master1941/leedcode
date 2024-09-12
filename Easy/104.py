"""
Учитывая значение root двоичного дерева, верните значение его максимальной глубины.
Максимальная глубина бинарного дерева - это количество узлов на самом длинном пути от
корневого узла до самого дальнего конечного узла.

Пример 1:
Ввод: root = [3,9,20, null, null, 15,7]
Вывод: 3

Пример 2:
Ввод: root = [1, null, 2]
Вывод: 2
"""

from typing import Optional

import sys

sys.path.append("d:\Dev\leedcode")
from utils import TreeNode, buildTree


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1


if __name__ == "__main__":
    sol = Solution()
    null = None

    root = [3, 9, 20, null, null, 15, 7]  # Вывод: 3
    root_1 = buildTree(root)
    print(sol.maxDepth(root_1))

    root = [1, null, 2]  # Вывод: 2
    root_1 = buildTree(root)
    print(sol.maxDepth(root_1))

    root = [1, null, 2, null, 3, null, 4, null, 5, null, 6, null, 7]
    root_1 = buildTree(root)
    print(sol.maxDepth(root_1))  # Output: 7
