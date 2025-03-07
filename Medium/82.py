"""
Учитывая head отсортированного связанного списка,
удалите все узлы с повторяющимися номерами,
оставив только уникальные номера из исходного списка.
Верните связанный список,также отсортированный

Пример 1:

Ввод: head = [1,2,3,3,4,4,5]
Вывод: [1,2,5]
Пример 2:

Ввод: head = [1,1,1,2,3]
Вывод: [2,3]

Ограничения:

Количество узлов в списке находится в диапазоне [0, 300].
-100 <= Node.val <= 100
Список гарантированно будет отсортирован в порядке возрастания.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ """
        result = ListNode()
        current = result
        f = 101

        while head:
            if head.next:
                head2 = head.next
                f2 = head2.val
            else:
                f2 = 101
            if f != head.val and head.val != f2:
                current.next = head
                current = current.next
            f = head.val
            head = head.next

        return result.next


def create_linked_list(listA: list) -> ListNode:
    """Генератор связных списков."""
    head_a = ListNode()
    current_a = head_a
    for i in range(len(listA)):
        current_a.next = ListNode(listA[i])
        current_a = current_a.next
    return head_a.next


if __name__ == "__main__":
    sol = Solution()
    # создание связных списков

    head = [1, 1, 1, 2, 3]

    listA = create_linked_list(head)

    d = sol.deleteDuplicates(listA)

    while d is not None:
        print(d.val)
        d = d.next

    print("/n")
    head = [1, 2, 3, 3, 4, 4, 5]
    listA = create_linked_list(head)

    d = sol.deleteDuplicates(listA)

    while d is not None:
        print(d.val)
        d = d.next
