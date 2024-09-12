"""
94. Обход бинарного дерева по порядку

Учитывая root двоичное дерево, верните обход значений его узлов по порядку."""

from typing import List, Optional
import sys
sys.path.append('d:\Dev\leedcode')
from utils import TreeNode, buildTree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Двоичное дерево, вернёт обход значений его узлов по порядку."""
        result = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)

        traverse(root)
        return result


if __name__ == "__main__":
    sol = Solution()
    null = None

    root = [1, null, 2, 3]
    root_1 = buildTree(root)
    print(sol.inorderTraversal(root_1))  # Output: [1, 3, 2]

    root = []
    root_1 = buildTree(root)
    print(sol.inorderTraversal(root_1))  # Output: []

    root = [1]
    root_1 = buildTree(root)
    print(sol.inorderTraversal(root_1))  # Output: [1]

    root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
    root_1 = buildTree(root)
    print(sol.inorderTraversal(root_1))  # Output: [4,2,6,5,7,1,3,9,8]

    root_1 = TreeNode(1)
    root_1.right = TreeNode(2)
    root_1.left = TreeNode(22)
    root_1.right.right = TreeNode(4)
    root_1.right.left = TreeNode(3)
    root_1.right.left.right = TreeNode(5)
    # Create the binary tree:
    #       1
    #      / \
    #     22  2
    #        /  \
    #       3    4
    #        \
    #         5

    print(sol.inorderTraversal(root_1))  # Output: [22, 1, 3, 5, 2, 4]
