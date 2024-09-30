from typing import Optional
import sys

sys.path.append("d:\Dev\leedcode")
from utils import TreeNode, buildTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Учитывая корни двух двоичных деревьев p и q, проверяет совпадают ли они или нет.
        Два бинарных дерева считаются одинаковыми, если они структурно идентичны,
        а узлы имеют одинаковое значение."""
        # if p.left == q.left is None and p.val == q.val and p.right == q.right is None:
        #     return True
        if (
            p.val != q.val
            or (p.left is None) ^ (q.left is None)
            or (p.right is None) ^ (q.right is None)
        ):
            return False
        return (
            (p.left is None and q.left is None) or self.isSameTree(p.left, q.left)
        ) and (
            (p.right is None and q.right is None) or self.isSameTree(p.right, q.right)
        )


if __name__ == "__main__":
    sol = Solution()
    null = None
    # Входные данные:
    p = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 43]
    q = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 43]  # Вывод: true
    root_q = buildTree(q)
    root_p = buildTree(p)
    print(sol.isSameTree(root_p, root_q))

    # Входные данные:
    p = [1, 2]
    q = [1, null, 2]  # Вывод: false
    root_q = buildTree(q)
    root_p = buildTree(p)
    print(sol.isSameTree(root_p, root_q))
    # Входные данные:
    p = [1, 2, 1]
    q = [1, 1, 2]  # Вывод: false
    root_q = buildTree(q)
    root_p = buildTree(p)
    print(sol.isSameTree(root_p, root_q))
