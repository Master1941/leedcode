'''
2. Сложите два числа
Средний
Темы
Компании
Вам предоставлены два непустых связанных списка, представляющих два
неотрицательных целых числа. Цифры хранятся в обратном порядке,
и каждый из их узлов содержит одну цифру. Сложите два числа и
верните сумму в виде связанного списка.

Вы можете предположить, что эти два числа не содержат никакого
начального нуля, за исключением самого числа 0.

Пример 1:
Ввод: l1 = [2,4,3], l2 = [5,6,4]
Вывод: [7,0,8]
Пояснение: 342 + 465 = 807.

Пример 2:
Ввод: l1 = [0], l2 = [0]
Вывод: [0]

Пример 3:
Ввод: l1 = [9,9,9,9,9,9], l2 = [9,9,9,9]
Вывод: [8,9,9,9,0,0,0,1]


Ограничения:

Количество узлов в каждом связанном списке находится в диапазоне [1, 100].
0 <= Node.val <= 9
Гарантируется, что список представляет собой число,
в котором нет начальных нулей.
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = current = ListNode()
        a = 0
        while a or l1 or l2:
            summ = 0
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            if a:
                summ += a
            a = summ // 10
            current.next = ListNode(summ % 10)
            current = current.next

        return result.next


def create_linked_list(listA: list, listB: list) -> list[ListNode]:
    """Генератор связных списков."""
    head_b = ListNode(listB[0])
    head_a = ListNode(listA[0])
    current_a = head_a
    current_b = head_b
    for i in listA[1:]:
        current_a.next = ListNode(i)
        current_a = current_a.next

    for i in listB[1:]:
        current_b.next = ListNode(i)
        current_b = current_b.next

    return head_a, head_b


def foo(l3: Optional[ListNode]) -> list:
    while l3:
        print(l3.val)
        l3 = l3.next


if __name__ == "__main__":
    sol = Solution()

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]  # Вывод:[7,0,8]
    listA, listB = create_linked_list(l1, l2)
    print(sol.addTwoNumbers(listA, listB))
    foo(sol.addTwoNumbers(listA, listB))

    l1 = [0]
    l2 = [0]  # Вывод:[0]
    listA, listB = create_linked_list(l1, l2)
    print(sol.addTwoNumbers(listA, listB))
    foo(sol.addTwoNumbers(listA, listB))

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]  # Вывод: [8,9,9,9,0,0,0,1]
    listA, listB = create_linked_list(l1, l2)
    print(sol.addTwoNumbers(listA, listB))
    foo(sol.addTwoNumbers(listA, listB))
