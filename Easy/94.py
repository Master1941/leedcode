"""
94. Обход бинарного дерева по порядку

Учитывая root двоичное дерево, верните обход значений его узлов по порядку. """

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Двоичное дерево, вернёт обход значений его узлов по порядку."""
        result =[]
        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)

        traverse(root)
        return result


def buildTree(values):
    """Строить бинарное дерево из списка."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    sol = Solution()
    null = None

    root = [1, null, 2, 3]
    root = buildTree(root)
    print(sol.inorderTraversal(root))  # Output: [1, 3, 2]

    root = [] 
    root = buildTree(root)
    print(sol.inorderTraversal(root)) # Output: []

    root = [1]
    root = buildTree(root)
    print(sol.inorderTraversal(root))  # Output: [1]

    root = [1,2,3,4,5, null,8,null, null, 6,7,9]
    root = buildTree(root)
    print(sol.inorderTraversal(root))  # Output: [4,2,6,5,7,1,3,9,8]

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(22)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.left.right = TreeNode(5)
    # Create the binary tree:
        #       1
        #      / \
        #     22  2
        #        /  \
        #       3    4
        #        \
        #         5
  
    print(sol.inorderTraversal(root))  # Output: [22, 1, 3, 5, 2, 4]