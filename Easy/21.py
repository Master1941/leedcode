"""
Вам будут предоставлены заголовки двух отсортированных
связанных списков list1 и list2.

Объедините два списка в один отсортированный список.
Список должен быть составлен путем объединения узлов первых двух списков.

Возвращает заголовок объединенного связанного списка.

Пример 1:

Ввод: list1 = [1,2,4], list2 = [1,3,4]
Вывод: [1,1,2,3,4,4]
Пример 2:

Ввод: list1 = [], list2 = []
Вывод: []
Пример 3:

Ввод: list1 = [], list2 = [0]
Вывод: [0]

Ограничения:

Количество узлов в обоих списках находится в диапазоне [0, 50].
-100 <= Node.val <= 100
Оба list1 и list2 отсортированы в неубывающем порядке.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        result = ListNode()
        current = result
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        if list1 is None:
            current.next = list2
        elif list2 is None:
            current.next = list1

        return result.next


def create_linked_list(listA: list) -> ListNode:
    """Генератор связных списков."""
    head_a = ListNode(listA[0])
    current_a = head_a
    for i in range(1, len(listA)):
        current_a.next = ListNode(listA[i])
        current_a = current_a.next
    return head_a


if __name__ == "__main__":
    sol = Solution()
    # создание связных списков
    listA = [1, 2, 4, 5, 6, 7, 8, 9]
    listB = [1, 3, 4]
    listA = create_linked_list(listA)
    listB = create_linked_list(listB)
    # listA = []
    # listB = []

    d = sol.mergeTwoLists(listA, listB)

    while d is not None:
        print(d.val)
        d = d.next
