"""
199. Вид двоичного дерева справа
Средний
Темы
Компании
Учитывая root двоичного дерева, представьте, что вы стоите справа от него, и верните значения узлов, которые вы видите, в порядке сверху вниз.


Пример 1:
Входные данные: root = [1, 2, 3, null, 5, null, 4]
Результат: [1,3,4]

Пример 2:
Входные данные: root = [1, 2, 3, 4, null, null, null, 5]
Результат: [1,3,4,5]

Пример 3:
Входные данные: root = [1,null,3]
Результат: [1,3]

Пример 4:
Входные данные: root = []
Результат: []


Ограничения:
Количество узлов в дереве находится в диапазоне [0, 100].
-100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional, List

null = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [root.val]
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                result.append(queue[-1].val)
        return result


def build_tree_from_array(arr):
    """Преобразование массива в бинарное дерево."""
    if not arr or len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1  # Индекс для прохода по массиву
    while queue and i < len(arr):
        node = queue.popleft()  # Извлекаем первый элемент из очереди
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    sol = Solution()

    # Входные данные
    arr = [1, 2, 3, null, 5, null, 4]
    # Преобразование массива в дерево
    tree_root = build_tree_from_array(arr)
    # Обход дерева уровнями
    result = sol.rightSideView(tree_root)
    print(result)  # Output: [1,3,4]

    # Входные данные
    arr = [1, 2, 3, 4, null, null, null, 5]
    # Преобразование массива в дерево
    tree_root = build_tree_from_array(arr)
    # Обход дерева уровнями
    result = sol.rightSideView(tree_root)
    print(result)  # Output: [1,3,4,5]

    # Входные данные
    arr = [1, null, 3]
    # Преобразование массива в дерево
    tree_root = build_tree_from_array(arr)
    # Обход дерева уровнями
    result = sol.rightSideView(tree_root)
    print(result)  # Output: [1,3]

    # Входные данные
    arr = []
    # Преобразование массива в дерево
    tree_root = build_tree_from_array(arr)
    # Обход дерева уровнями
    result = sol.rightSideView(tree_root)
    print(result)  # Output: []

    # Создание бинарного дерева
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    # Вызов функции обхода
    result = sol.rightSideView(root)
    print(result)  # Output: [1, 3, 7, 8]
